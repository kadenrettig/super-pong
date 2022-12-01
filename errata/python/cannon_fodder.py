# KADEN RETTIG, CPSC 4160, FALL 2022
# main for cannon fodder simulation

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
timer_actions = []
box_colliders = []
particles = []
boxes = []


#################################### VIEWER ####################################
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

display = pl.make_display_screen_action()
resizer = pl.make_screen_resize_action() 
viewer = pl.make_frame_viewer( (SCREEN_WIDTH, SCREEN_HEIGHT) )
viewer_actions.append( pl.make_close_viewer_action() )
viewer_actions.append( display )
viewer_actions.append( resizer )
game_content.append( viewer )


##################################### TIMER ####################################
# make the timer
timer = util.make_timer()

# add start action
start = util.make_start_action()
timer_actions.append( start )

# add update action
timer_actions.append( util.make_update_action() )

# alarm to activate the rect collider
alarm = util.make_alarm_action( 9000, False ) 
timer_actions.append( alarm )


#################################### CIRCLES ###################################
COLLIDER_CUTOFF = 380

# create a list of circles to be used as particles
def get_circles(nx, ny, nb):
  circles = []
  radius = 10
  for i in range( 0, nb ):
    circle_bounds = ( random.randint(0, nx-COLLIDER_CUTOFF), 
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

circs = get_circles( SCREEN_WIDTH, SCREEN_HEIGHT, 100 )


#################################### PHYSICS ###################################
# generate physics & particles for each circle
def get_particles(init_data):
  particles = [] 
  parts = phys.make_particles()
  deactivate_parts = phys.make_deactivate_action()
  activate_parts = phys.make_activate_action()
  parts.insert_action( deactivate_parts )
  parts.insert_action( activate_parts )
  particles.append( parts )
  
  for d in init_data:
    position = list( d.location )
    velocity = [ (20.0 * random.random() - 1.0), (2.0 * random.random() - 1.0) ]
    mass = 1.0
    parts.add_particle( position, velocity, mass )
    
  ### boundary detection ### 
  # right section of screen
  inside_right = act.make_is_inside_action()
  inside_right.children.append( deactivate_parts )
  right_rect = act.make_rectangle( ((925, 0, 1300, 740), 
                                    (100, 46, 50)) )
  #right_rect.insert_action( act.make_draw_rectangle_action() )
  right_rect.insert_action( inside_right )
  game_content.append( right_rect )
  display.insert_entity( right_rect )
  
  # left section of screen
  inside_left = act.make_is_inside_action()
  inside_left.children.append( deactivate_parts )
  left_rect = act.make_rectangle( ((0, 0, 925, SCREEN_HEIGHT), 
                                   (0, 46, 68)) )
  #left_rect.insert_action( act.make_draw_rectangle_action() )
  left_rect.insert_action( inside_left )
  game_content.append( left_rect )
  display.insert_entity( left_rect )
  
  ### forces ###
  # spring force
  spring = phys.make_spring_force()
  spring.spring_constant = 0.004
  spring_action = phys.make_spring_action()
  spring.insert_action( spring_action )
  spring_action.children.append( inside_right )
  spring_action.children.append( activate_parts )
  
  # gravity 
  gravity = phys.make_gravity_force()
  gravity.gravity = [0.0, 0.6]
  grav_action = phys.make_gravity_action() 
  gravity.insert_action( grav_action )
  
  # drag 
  drag = phys.make_drag_force()
  drag.drag_constant = 0.015
  drag_action = phys.make_drag_action()
  drag.insert_action( drag_action )
  drag_action.children.append( inside_left )
  drag_action.children.append( activate_parts )
  
  ### solvers ###
  # position solve 
  psolve = phys.make_position_solve_action() 
  parts.insert_action( psolve )
  
  # velocity solve
  vsolve = phys.make_velocity_solve_action() 
  parts.insert_action( vsolve ) 
  vsolve.children.append( spring_action )
  vsolve.children.append( grav_action )
  vsolve.children.append( drag_action )
  
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
  
  ### collisions with rectangles in play area ###
  # bottom half of column
  box_colliders.append( ( ([900, 420], [950, 750]),   # llc, urc
                          (255, 255, 255),            # color
                          True ) )                    # active
  # top half of column
  box_colliders.append( ( ([900, 0], [950, 330]), 
                          (255, 255, 255), 
                          True ) )
  # gap between column halves
  box_colliders.append( ( ([900, 325], [950, 425]), 
                          (255, 255, 255), 
                          False ) )
  # platform #1 right side
  box_colliders.append( ( ([1000, 530], [1100, 545]), 
                          (255, 255, 255), 
                          True ) )
  # platform # 2 right side
  box_colliders.append( ( ([1150, 560], [1250, 575]), 
                          (255, 255, 255), 
                          True ) )
  
  # create box colliders
  for b in box_colliders:
    box_collider = phys.make_rectangle_collider( b[0][0], b[0][1] )
    outside_collisions = phys.make_outside_rectangle_collision() 
    box_collider.insert_action( outside_collisions )
    psolve.children.append( outside_collisions )
    box_collider.active = b[2]
    
    # attach activate action if required
    if b[2] == False:
      activate_action = util.make_activate_action()
      box_collider.insert_action( activate_action )
      alarm.children.append( activate_action )
  
  return particles

# create every particle for simulation
particles = get_particles( circs )


##################################### BOXES ####################################
# create all rectangles that represent each rectangular collider
def get_boxes(init_data):
  boxes = []
  for b in init_data:
    rect_loc = ( b[0][0] )
    rect_dim = ( abs(b[0][0][0] - b[0][1][0]), abs(b[0][0][1] - b[0][1][1]) )
    rect_col = ( b[1] )
    rect = act.make_rectangle(  ((rect_loc[0], rect_loc[1], 
                                  rect_dim[0], rect_dim[1]), 
                                  rect_col) )
    rect.insert_action( act.make_draw_rectangle_action() )
    rect.active = b[2]
    
    # attach activate action if required
    if b[2] == False:
      activate_action = util.make_activate_action()
      rect.insert_action( activate_action )
      alarm.children.append( activate_action )
    boxes.append( rect )
  return boxes

# create rectangles for each collider
boxes = get_boxes( box_colliders )


################################ APPEND CONTENT ################################
# add actions to viewer
for action in viewer_actions:
  viewer.insert_action( action )
  print( f"Loading {action.name} into viewer..." )

# add actions to timer
for action in timer_actions:
  print( f"Loading timer {action.name}..." )
  timer.insert_action( action )
  
# append all game content
print( f"Loading game content..." )
game_content = game_content + circs + particles + boxes
game_content.append( timer )

# append all display items
print( f"Loading items into display..." )
for b in circs + boxes:
  display.insert_entity( b )


################################# GAME LOOPER ##################################
# make the game loop & loop
looper = pl.make_game_looper( game_content )
looper.loop()