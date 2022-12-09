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
    if self.condition_to_act(data):
      
      # get new counter values 
      for c in self.children:
        if c.name == "player_1_counter":
          self.player_1_score = c.counter
        if c.name == "player_2_counter":
          self.player_2_score = c.counter
      
      # update the counter displays
      for c in self.entity_state.children:
        if c.name == "player_1_hud":
          c.text = f"{self.player_1_score}"
        if c.name == "player_2_hud":
          c.text = f"{self.player_2_score}"
      
      # wait to be moved again
      self.active = False
    return

################################## CONTAINERS ##################################
game_content = [] # Persistent Game Content
viewer_actions = [] # Persistent Viewer Actions

level_content = [] # Level specific content
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
move_player_one_paddle = act.make_move_player_action( 0.5 )
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
move_player_two_paddle = act.make_move_player_action( 0.5 )
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
net_part_1 = act.make_rectangle((((SCREEN_WIDTH/2) - 10, 0, 10, 110), 
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


player_1_goal.insert_action(act.make_draw_rectangle_action()) 
level_content.append( player_1_goal )

player_2_goal = act.make_rectangle(((SCREEN_WIDTH-30,0, 30, SCREEN_HEIGHT),(255,255,255), "player_2_goal"))
player_2_scorer = act.make_index_is_inside_action(0)
player_2_goal.insert_action( player_2_scorer )
player_2_scorer.children.append( particle_reset )

player_2_goal.insert_action(act.make_draw_rectangle_action()) 
level_content.append( player_2_goal )

### Points ###
# player 1 counter
player_1_counter = util.make_counter("player_1_counter")
player_1_increment = util.make_increment_action( 1 )
player_1_reset = util.make_reset_action( 0 )
player_2_scorer.children.append( player_1_increment )
player_1_counter.insert_action( player_1_increment )
player_1_counter.insert_action( player_1_reset )

# player 2 counter 
player_2_counter = util.make_counter("player_2_counter")
player_2_increment = util.make_increment_action( 1 )
player_2_reset = util.make_reset_action( 0 )
player_1_scorer.children.append( player_2_increment )
player_2_counter.insert_action( player_2_increment )
player_2_counter.insert_action( player_2_reset )


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

# hud message generater for counters
generate_message.children.append( player_1_counter )
generate_message.children.append( player_2_counter )
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
def get_particles(init_data):
  # initialize particle entity
  particles = [] 
  parts = phys.make_particles()
  particles.append( parts )
  
  # create particles for each given circle
  for d in init_data:
    position = list( d.location )
    velocity = [ (2.0 * random.random() - 2.0), (2.0 * random.random() - 1.0) ]
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
  esolve.dt = 0.6
  parts.insert_action( esolve )
  esolve.children.append( psolve )
  esolve.children.append( vsolve )
  esolve.types.append( "loop" )
  
  # connect particle positions to circle positions
  for i in range( 0, len(init_data) ):
    pick = phys.make_pick_position_action( i )
    put = act.make_put_position_action()
    
    parts.insert_action( pick )
    init_data[i].insert_action( put )
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
  
  return particles

# create every particle for simulation
particles = get_particles( circs )

# Add reset to particles
particles[0].insert_action( particle_reset )


################################ APPEND CONTENT ################################
# add actions to viewer
for action in viewer_actions:
  viewer.insert_action( action )
  print( f"Loading {action.name} into viewer..." )
  
# append all game content
print( f"Loading game content..." )
level_content = level_content + circs + particles


################################# GAME LOOPER ##################################
# make the game loop & loop
looper = pl.make_game_looper( game_content )

# Start button
start_button = ui.make_button( ((305, 110, 200, 200), (0,255,0), "start_button"))
start_button.insert_action(ui.make_draw_rect_button_action())
start_press = ui.make_button_press_action()
start_button.insert_action(start_press)
looper.insert_entity(start_button)
display.insert_entity(start_button)

# End button
end_button = ui.make_button( ((805, 110, 200, 200), (255,0,0), "end_button"))
end_button.insert_action(ui.make_draw_rect_button_action())
end_press = ui.make_button_press_action()
end_button.insert_action(end_press)
looper.insert_entity(end_button)
display.insert_entity(end_button)

# Levels
test_level = pl.make_level(looper, display, level_content, "test_level")
loader = pl.make_load_level_action()
test_level.insert_action(loader)
start_press.children.append(loader)

closer = pl.make_close_level_action()
test_level.insert_action(closer)
end_press.children.append(closer)
end_press.children.append(particle_reset)
end_press.children.append(player_1_reset)
end_press.children.append(player_2_reset)


looper.loop()
