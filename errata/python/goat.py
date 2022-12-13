# ADAM COPELAND, STEPHEN SAMS, KADEN RETTIG
# CPSC 4160, FALL 2022

import sys
sys.path.insert( 0, "./" )
import os
import random
import pygame
from pygame.locals import *

import errata.engine.utility as util
import errata.engine.physics as phys
import errata.assets.sounds as sound
import errata.engine.actor as act 
import errata.engine.sound as sfx
import errata.engine.play as pl 
import errata.engine.ui as ui
import errata.python as py

# Score Specific to this Game
class GenerateMessage():
  def __init__(self):
    self.player_1_score = 0
    self.player_2_score = 0
    self.level_count = 0
    self.types = ["display"]
    self.entity_state = None
    self.name = "generate_message_action"
    self.children = []
    self.active = False
    self.verbose = False 
    return
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False
    if data == None:
      return False
    return True
  
  def act(self, data):
    if self.condition_to_act( data ):
      
      # get new counter values 
      for c in self.children:
        if c.name == "player_1_counter":
          self.player_1_score = c.counter
        if c.name == "player_2_counter":
          self.player_2_score = c.counter
        if c.name == "level_counter":
          self.level_count = c.counter
      
      # update the counter displays
      for c in self.entity_state.children:
        if c.name == "player_1_hud":
          c.text = f"{self.player_1_score}"
        if c.name == "player_2_hud":
          c.text = f"{self.player_2_score}"
        if c.name == "level_hud":
          c.text = f"Level {self.level_count}"
      
      # wait to be moved again
      self.active = False
    return
  
# action to add a new obstacle to the level with each iteration
class AddObstacles():
  def __init__(self):
    self.types = ["display"]
    self.obstacles = []
    self.entity_state = None 
    self.name = "add_obstacles_action"
    self.children = []
    self.active = True 
    self.verbose = False 
    return 
  
  def condition_to_act(self, data):
    if data == None:
      return False
    return True
  
  def act(self, data):
    if self.condition_to_act( data ):
      
      for i in range(0, data):
        # create new obstacle
        # obs_dimensions = (random.randint(25,50), random.randint(25, 50))
        obs_dimensions = (45, 45)
        obs_location = (random.randint(50, SCREEN_WIDTH - obs_dimensions[0] - 50), 
                        random.randint(51, SCREEN_HEIGHT - obs_dimensions[1])) 
        obs_color = (random.randint(15, 255), random.randint(15, 255), 
                     random.randint(15, 255))
        obs_info = ( (obs_location + obs_dimensions), obs_color, 
                     "obs_rect" ) 
        obs_rect = act.make_rectangle( obs_info )
        obs_drawer = act.make_draw_rectangle_action()
        obs_rect.insert_action( obs_drawer )
        
        # create collider for the obstacle
        obs_collider = phys.make_rectangle_collider( (obs_location[0], obs_location[1]), 
                                                     (obs_location[0] + obs_dimensions[0], 
                                                      obs_location[1] + obs_dimensions[1]) )
        obs_collision = phys.make_outside_rectangle_collision()
        obs_collider.insert_action( obs_collision )

        # Ensure colliders only work for active particles
        obs_collider.active = False
        obs_activator = util.make_activate_action()
        obs_collider.insert_action(obs_activator)
        obs_drawer.children.append(obs_activator)
        
        # append new rect + collider to list
        self.obstacles.append( (obs_rect, obs_collider) )
      
    return self.obstacles


################################## CONTAINERS ##################################
game_content = [] # Persistent Game Content
viewer_actions = [] # Persistent Viewer Actions

level_content = [] # Level specific content
levels = [] # List of levels
hud_actions = []
box_colliders = []
particles = []


#################################### VIEWER ####################################
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

display = pl.make_display_screen_action() 
viewer = pl.make_frame_viewer( (SCREEN_WIDTH, SCREEN_HEIGHT) )
viewer.set_title("SuperPong")
viewer_actions.append( pl.make_close_viewer_action() )
viewer_actions.append( display )
viewer_actions.append( pl.make_screen_resize_action() )
game_content.append( viewer )


#################################### SOUND #####################################
# path for sound assets
sound_path = str( os.path.abspath(sound.__file__) )
sound_path = sound_path[:len(sound_path)-11]

# initialize mixer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

# background music
hyron_bgm = sfx.make_track( sound_path, "hyron.mp3" )
hyron_bgm.insert_action( sfx.make_bgm_action( -1 ) )
pygame.mixer.music.set_volume( 0.3 )
game_content.append( hyron_bgm )

# retro scoring sound 
score_sound = sfx.make_sound_action( sound_path + 
                                     "mixkit-retro-game-notification-212.wav" )

# retro level end sound
end_sound = sfx.make_sound_action( sound_path + 
                                   "mixkit-arcade-retro-game-over-213.wav" )


#################################### CIRCLES ###################################
# create a list of circles to be used as particles
def get_circles(nx, ny, nb):
  circles = []
  radius = 10
  for i in range( 0, nb ):
    circle_bounds = ( SCREEN_WIDTH/2, SCREEN_HEIGHT/2 )
    circle_color  = ( random.randint(0, 255), 
                      random.randint(0, 255), 
                      random.randint(0, 255))
    # radius, location, color, name
    circle = act.make_circle( (radius, 
                               circle_bounds, 
                               circle_color, 
                               f"circle_{i}") )
    circle.insert_action( act.make_draw_circle_action() )
    circles.append( circle )
  return circles

circs = get_circles( SCREEN_WIDTH, SCREEN_HEIGHT, 1 )


################################## PLAYERS #####################################
##### player 1 #####
# player 1 paddle
player_one_paddle = act.make_rectangle( ( (30, SCREEN_HEIGHT/2, 20, 200), 
                                          (50, 100, 83), 
                                          "player_one_paddle_rect") )
player_one_paddle.insert_action( act.make_draw_rectangle_action() )
move_player_one_paddle = act.make_move_player_action( 2.5, SCREEN_WIDTH, SCREEN_HEIGHT )
player_one_paddle.insert_action( move_player_one_paddle )
move_player_one_paddle.children.append( player_one_paddle )

# player 1 controller
player_one_key_list = ( K_w, K_s, None, None )
player_one_controller = act.make_player_controller_action( player_one_key_list )
player_one_paddle.insert_action( player_one_controller )
player_one_controller.children.append( move_player_one_paddle )

##### player 2 #####
# player 2 paddle
player_two_paddle = act.make_rectangle( ( (SCREEN_WIDTH-50, SCREEN_HEIGHT/2, 20, 200),
                                          (50, 100, 83), 
                                          "player_two_paddle_rect") )
player_two_paddle.insert_action( act.make_draw_rectangle_action() )
move_player_two_paddle = act.make_move_player_action( 2.5, SCREEN_WIDTH, SCREEN_HEIGHT )
player_two_paddle.insert_action( move_player_two_paddle )
move_player_two_paddle.children.append( player_two_paddle )

# player 2 controller
player_two_key_list = ( K_UP, K_DOWN, None, None ) 
player_two_controller = act.make_player_controller_action( player_two_key_list )
player_two_paddle.insert_action( player_two_controller )
player_two_controller.children.append( move_player_two_paddle )

##### prepare to instantiate #####
level_content.append( player_one_paddle )
level_content.append( player_two_paddle )

########################## POINTS AND GAMEPLAY THINGS ##########################
###### game net ######
net_part_1 = act.make_rectangle((((SCREEN_WIDTH/2) - 10, 60, 10, 50), 
                                 (50, 100, 83),
                                 "net_part_1_rectangle"))
net_part_1.insert_action(act.make_draw_rectangle_action()) 
level_content.append( net_part_1 )

net_part_2 = act.make_rectangle((((SCREEN_WIDTH/2) - 10, 120, 10, 110), 
                                 (50, 100, 83),
                                 "net_part_1_rectangle"))
net_part_2.insert_action(act.make_draw_rectangle_action()) 
level_content.append( net_part_2 )

net_part_3 = act.make_rectangle((((SCREEN_WIDTH/2) - 10, 240, 10, 110), 
                                 (50, 100, 83),
                                 "net_part_1_rectangle"))
net_part_3.insert_action(act.make_draw_rectangle_action()) 
level_content.append( net_part_3 )

net_part_4 = act.make_rectangle((((SCREEN_WIDTH/2) - 10, 360, 10, 110), 
                                 (50, 100, 83),
                                 "net_part_1_rectangle"))
net_part_4.insert_action(act.make_draw_rectangle_action()) 
level_content.append( net_part_4 )

net_part_5 = act.make_rectangle((((SCREEN_WIDTH/2) - 10, 480, 10, 110), 
                                 (50, 100, 83),
                                 "net_part_5_rectangle"))
net_part_5.insert_action(act.make_draw_rectangle_action()) 
level_content.append( net_part_5 )

net_part_6 = act.make_rectangle((((SCREEN_WIDTH/2) - 10, 600, 10, 120), 
                                 (50, 100, 83),
                                 "net_part_6_rectangle"))
net_part_6.insert_action(act.make_draw_rectangle_action()) 
level_content.append( net_part_6 )

# Particle Reset
particle_reset = phys.make_reset_particle_action(0, [SCREEN_WIDTH/2, SCREEN_HEIGHT/2])

### Goals ###
player_1_goal = act.make_rectangle(((0,0, 30, SCREEN_HEIGHT),(255,255,255), "player_1_goal"))
player_1_scorer = act.make_index_is_inside_action(0)
player_1_goal.insert_action( player_1_scorer )
player_1_scorer.children.append( particle_reset )
player_1_scorer.children.append( score_sound )

player_1_goal.insert_action(act.make_draw_rectangle_action()) 
level_content.append( player_1_goal )

player_2_goal = act.make_rectangle(((SCREEN_WIDTH-30,0, 30, SCREEN_HEIGHT),(255,255,255), "player_2_goal"))
player_2_scorer = act.make_index_is_inside_action(0)
player_2_goal.insert_action( player_2_scorer )
player_2_scorer.children.append( particle_reset )
player_2_scorer.children.append( score_sound )

player_2_goal.insert_action(act.make_draw_rectangle_action()) 
level_content.append( player_2_goal )

### Points ###
# player 1 counter
player_1_counter = util.make_counter("player_1_counter")
player_1_increment = util.make_increment_action( 1 )
player_1_reset = util.make_reset_action(0)
player_1_trigger = util.make_count_trigger_action(3)
player_1_trigger.children.append( end_sound )
player_2_scorer.children.append( player_1_increment )
player_2_scorer.children.append( player_1_trigger )
player_1_counter.insert_action( player_1_increment )
player_1_counter.insert_action( player_1_reset)
player_1_counter.insert_action( player_1_trigger)

# player 2 counter 
player_2_counter = util.make_counter("player_2_counter")
player_2_increment = util.make_increment_action( 1 )
player_2_reset = util.make_reset_action(0)
player_2_trigger = util.make_count_trigger_action(3)
player_2_trigger.children.append( end_sound )
player_1_scorer.children.append( player_2_increment )
player_1_scorer.children.append( player_2_trigger )
player_2_counter.insert_action( player_2_increment )
player_2_counter.insert_action( player_2_reset )
player_2_counter.insert_action( player_2_trigger)

# level counter 
level_counter = util.make_counter("level_counter")
level_increment = util.make_increment_action( 1 )
level_counter.insert_action( level_increment )

# Speed Increase
speed_increase = phys.make_increase_speed_action(0, [0.1, 0.1])

###################################### HUD #####################################
# hud message generation action
generate_message = GenerateMessage()

# hud creation
hud = ui.make_hud()

# hud counter for player 1 score appearances
# font size, location, color, text
hud_player_1 = act.make_text( (50, 
                              (270, 15), 
                              (255, 255, 255), 
                              "0", 
                              "player_1_hud") )
hud_player_1.insert_action( act.make_draw_text_action() )
hud.children.append( hud_player_1 )

# hud counter for player 2's score
hud_player_2 = act.make_text( (50, 
                              (960, 15), 
                              (255, 255, 255), 
                              "0", 
                              "player_2_hud"))
hud_player_2.insert_action( act.make_draw_text_action() )
hud.children.append( hud_player_2 )

# hud counter for the current level
hud_level = act.make_text( (50, 
                              (550, 15), 
                              (255, 255, 255), 
                              "Level 0", 
                              "level_hud"))
hud_level.insert_action( act.make_draw_text_action() )
hud.children.append ( hud_level )

# hud message generater for counters
generate_message.children.append( player_1_counter )
generate_message.children.append( player_2_counter )
generate_message.children.append( level_counter )
hud_actions.append( generate_message )

# draw the hud action
draw_hud = ui.make_draw_hud_action()
hud_actions.append( draw_hud )

# add actions to hud
for action in hud_actions:
  print(f"Loaded HUD {action.name}...")
  hud.insert_action( action )

# add complete hud to game content
level_content.append( hud )

                                            
#################################### PHYSICS ###################################
# generate physics & particles for each circle
# initialize particle entity
particles = [] 
parts = phys.make_particles()
particles.append( parts )

# create particles for each given circle
for d in circs:
  position = list( d.location )
  velocity = [1.0, 1.0 ]
  mass = 1.0
  parts.add_particle( position, velocity, mass )

##### solvers #####
# position solve 
psolve = phys.make_position_solve_action() 
parts.insert_action( psolve )

# velocity solve
vsolve = phys.make_velocity_solve_action() 
parts.insert_action( vsolve ) 

# Add goal checking actions to vsolve
vsolve.children.append( player_1_scorer )
vsolve.children.append( player_2_scorer )

# euler solve
esolve = phys.make_euler_solve_action() 
esolve.dt = 1.5
parts.insert_action( esolve )
esolve.children.append( psolve )
esolve.children.append( vsolve )
esolve.types.append( "loop" )

# connect particle positions to circle positions
for i in range( 0, len(circs) ):
  pick = phys.make_pick_position_action( i )
  put = act.make_put_position_action()
  
  parts.insert_action( pick )
  circs[i].insert_action( put )
  pick.children.append( put )
  
  esolve.children.append( pick )
  
##### collisions with paddles in play area #####
# collisions with the window frame
window_collider = phys.make_rectangle_collider( [0,0], 
                                                [SCREEN_WIDTH, SCREEN_HEIGHT] )
collisions = phys.make_inside_rectangle_collision()
window_collider.insert_action( collisions )
psolve.children.append( collisions )

# player paddle 1
box_colliders.append( ( ([30, SCREEN_HEIGHT/2], [50, 560]),   # llc, urc
                        (200,150,150),                        # color
                        True ) )                              # initial active state

# player paddle 2 
box_colliders.append( ( ([SCREEN_WIDTH-50, SCREEN_HEIGHT/2], [SCREEN_WIDTH-30, 560]),
                        (200, 150, 150), 
                        True ) )


# create box colliders
for b in box_colliders:
  box_collider = phys.make_rectangle_collider( b[0][0], b[0][1] )
  outside_collisions = phys.make_outside_rectangle_collision() 
  box_collider.insert_action( outside_collisions )
  psolve.children.append( outside_collisions )
  box_collider.active = b[2]
  if box_colliders.index( b ) == 0:
    move_player_one_paddle.children.append( box_collider )
  elif box_colliders.index( b ) == 1:
    move_player_two_paddle.children.append( box_collider )

# Add reset to particles
particles[0].insert_action( particle_reset )

# Add speed increase to particles
particles[0].insert_action( speed_increase )

level_content = level_content + circs + particles

### Generate levels
# create obstacles
add_obstacles_action = AddObstacles()
for i in range(0,23):
    current_level = []
    for content in level_content:
      current_level.append(content)
    obstacles = add_obstacles_action.act( 2 )
    for obstacle in obstacles:
      psolve.children.append( obstacle[1].actions[0] )
      current_level.append( obstacle[0] )
      current_level.append( obstacle[1] )
    levels.append(current_level)

################################ APPEND CONTENT ################################
# add actions to viewer
for action in viewer_actions:
  viewer.insert_action( action )
  print( f"Loading {action.name} into viewer..." )
  
# append all game content
print( f"Loading game content..." )
level_content = level_content


################################# CREDIT PAGE ##################################
credit_hud = ui.make_hud()
created_by = act.make_text( (35, 
                           (500, 295), 
                           (255, 255, 255), 
                           "CREATED BY:", 
                           "created_by_message") )
created_by.insert_action( act.make_draw_text_action() )
credit_hud.children.append( created_by )

kaden_rettig = act.make_text( (35, 
                           (500, 350), 
                           (255, 255, 255), 
                           "KADEN RETTIG", 
                           "kaden_message") )
kaden_rettig.insert_action( act.make_draw_text_action() )
credit_hud.children.append( kaden_rettig )

adam_copeland = act.make_text( (35, 
                           (500, 395), 
                           (255, 255, 255), 
                           "ADAM COPELAND", 
                           "adam_message") )
adam_copeland.insert_action( act.make_draw_text_action() )
credit_hud.children.append( adam_copeland )

stephen_sams = act.make_text( (35, 
                           (500, 440), 
                           (255, 255, 255), 
                           "STEPHEN SAMS", 
                           "stephen_message") )
stephen_sams.insert_action( act.make_draw_text_action() )
credit_hud.children.append( stephen_sams )
credit_hud.insert_action( ui.make_draw_hud_action() )

credit_screen = []
credit_screen.append(credit_hud)
levels.append(credit_screen)


################################# GAME LOOPER ##################################
# make the game loop & loop
looper = pl.make_game_looper( game_content )

# Start button
start_button = ui.make_button( ((415, 550, 400, 150), (50,100,83), "start_button"))
start_button.insert_action(ui.make_draw_rect_button_action())
start_button.border = True
start_button.border_thickness = 10
start_press = ui.make_button_press_action()
start_deactivate = util.make_deactivate_action()
start_activate = util.make_activate_action()
start_button.insert_action(start_press)

start_button.insert_action(start_deactivate)
start_button.insert_action(start_activate)

start_press.children.append(start_deactivate)

############################# START SCREEN TEXT ################################
start_screen_hud = ui.make_hud()

game_title = act.make_text( (75, 
                           (340, 25), 
                           (255, 255, 255), 
                           "SUPER   PONG", 
                           "game_title_message") )                
game_title.insert_action( act.make_draw_text_action() )

game_info_1 = act.make_text( (35, 
                           (135, 240), 
                           (255, 255, 255), 
                           "To progress to the next level be the first to score 3 points", 
                           "game_info_1_message") )                
game_info_1.insert_action( act.make_draw_text_action() )

game_info_2 = act.make_text( (35, 
                           (135, 285), 
                           (255, 255, 255), 
                           "Though the higher level, the higher the ball's speed and", 
                           "game_info_2_message") )                
game_info_2.insert_action( act.make_draw_text_action() )

game_info_3 = act.make_text( (35, 
                           (140, 330), 
                           (255, 255, 255), 
                           "the more obstacles that spawn to block its path", 
                           "game_info_3_message") )                
game_info_3.insert_action( act.make_draw_text_action() )

press_start = act.make_text( (35, 
                           (490, 615), 
                           (255, 255, 255), 
                           "PRESS START", 
                           "press_start_message") )                
press_start.insert_action( act.make_draw_text_action() )

#appending the necessary info to display to the hud
start_screen_hud.children.append( game_title )
start_screen_hud.children.append( game_info_1 )
start_screen_hud.children.append( game_info_2 )
start_screen_hud.children.append( game_info_3 )
start_screen_hud.children.append( press_start )

#inserting the start_screen_hud's actions
start_screen_hud.insert_action( ui.make_draw_hud_action())
start_hud_deactivate = util.make_deactivate_action()
start_hud_activate = util.make_activate_action()
start_screen_hud.insert_action(start_hud_deactivate)
start_screen_hud.insert_action(start_hud_activate)

#adds the start screen hud's deactivate to start_press so that,
#the text on the start screen goes away whent the levels start
start_press.children.append(start_hud_deactivate)

looper.insert_entity(start_button)
looper.insert_entity(start_screen_hud)
display.insert_entity(start_button)
display.insert_entity(start_screen_hud)
# DEBUG: End button
# end_button = ui.make_button( ((805, 110, 200, 200), (255,0,0), "end_button"))
# end_button.active = False
# end_deactivate = util.make_deactivate_action()
# end_activate = util.make_activate_action()

# end_button.insert_action(ui.make_draw_rect_button_action())
# end_press = ui.make_button_press_action()
# end_button.insert_action(end_press)

# end_button.insert_action(end_activate)
# end_button.insert_action(end_deactivate)

# start_press.children.append(end_activate)
# end_press.children.append(start_activate)
# end_press.children.append(end_deactivate)

# looper.insert_entity(end_button)
# display.insert_entity(end_button)

# Levels

levels.append(level_content)
level_manager = pl.make_level_manager(looper, display, levels, "level_manager")
level_loader = pl.make_load_level_action()
level_manager.insert_action(level_loader)
start_press.children.append(level_loader)

closer = pl.make_close_level_action()
level_manager.insert_action(closer)


# end_press.children.append(closer)
player_1_trigger.children.append(closer)
player_2_trigger.children.append(closer)

# Other actions to trigger on close
closer.children.append(particle_reset)
closer.children.append(player_1_reset)
closer.children.append(player_2_reset)
closer.children.append(speed_increase)
closer.children.append(level_loader)
level_loader.children.append(level_increment)

looper.loop()
