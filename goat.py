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

################################## CONTAINERS ##################################
game_content = []
viewer_actions = []
box_colliders = []
boxes = []
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
    circle_bounds = ( random.randint(0, nx), 
                      random.randint(0, ny) )
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
player_one_paddle = act.make_rectangle( ((30, SCREEN_HEIGHT/2, 20, 200), 
                                         (50, 100, 83), 
                                         "paddle") )
player_one_paddle.insert_action( act.make_draw_rectangle_action() )
move_player_one_paddle = act.make_move_player_action( 0.5 )
player_one_paddle.insert_action( move_player_one_paddle )
move_player_one_paddle.children.append(player_one_paddle)

# player 1 controller
key_list=(K_UP, K_DOWN, None, None) 
player_controller_one = act.make_player_controller_action( key_list )
player_one_paddle.insert_action( player_controller_one )
player_controller_one.children.append( move_player_one_paddle )

# add to display
display.insert_entity( player_one_paddle )
game_content.append( player_one_paddle )



##### player 2 #####
# player 2 paddle


#################################### PHYSICS ###################################
# generate physics & particles for each circle
def get_particles(init_data):
  particles = [] 
  parts = phys.make_particles()
  particles.append( parts )
  
  for d in init_data:
    position = list( d.location )
    velocity = [ (2.0 * random.random() - 2.0), (2.0 * random.random() - 1.0) ]
    mass = 1.0
    parts.add_particle( position, velocity, mass )
  
  ### solvers ###
  # position solve 
  psolve = phys.make_position_solve_action() 
  parts.insert_action( psolve )
  
  # velocity solve
  vsolve = phys.make_velocity_solve_action() 
  parts.insert_action( vsolve ) 

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
    
  # collisions with the window frame
  window_collider = phys.make_rectangle_collider( [0,0], 
                                                  [SCREEN_WIDTH, SCREEN_HEIGHT] )
  collisions = phys.make_inside_rectangle_collision()
  window_collider.insert_action( collisions )
  psolve.children.append( collisions )
  
  ### collisions with paddles in play area ###
  # player paddle 1
  box_colliders.append( ( ([30, SCREEN_HEIGHT/2], [50, 560]),   # llc, urc
                          (200,150,150),            # color
                          True ) )                    # active
  
  # move_colliders = act.make_move_player_action( 0.5 )

  # create box colliders
  for b in box_colliders:
    box_collider = phys.make_rectangle_collider( b[0][0], b[0][1] )
    outside_collisions = phys.make_outside_rectangle_collision() 
    box_collider.insert_action( outside_collisions )
    psolve.children.append( outside_collisions )
    box_collider.active = b[2]
    move_player_one_paddle.children.append(box_collider)
  
  return particles

# create every particle for simulation
particles = get_particles( circs )
 
 
##################################### BOXES ####################################
# # create all rectangles that represent each rectangular collider
# def get_boxes(init_data):
#   boxes = []
#   for b in init_data:
#     rect_loc = ( b[0][0] )
#     rect_dim = ( abs(b[0][0][0] - b[0][1][0]), abs(b[0][0][1] - b[0][1][1]) )
#     rect_col = ( b[1] )
#     rect = act.make_rectangle(  ((rect_loc[0], rect_loc[1], 
#                                   rect_dim[0], rect_dim[1]), 
#                                   rect_col) )
#     rect.insert_action( act.make_draw_rectangle_action() )
#     rect.active = b[2]

#     boxes.append( rect )
#   return boxes

# # create rectangles for each collider
# boxes = get_boxes( box_colliders )





################################ APPEND CONTENT ################################
# add actions to viewer
for action in viewer_actions:
  viewer.insert_action( action )
  print( f"Loading {action.name} into viewer..." )
  
# append all game content
print( f"Loading game content..." )
game_content = game_content + circs + particles + boxes

# append all display items
print( f"Loading items into display..." )
for e in circs + boxes:
  display.insert_entity( e )


################################# GAME LOOPER ##################################
# make the game loop & loop
looper = pl.make_game_looper( game_content )
looper.loop()
