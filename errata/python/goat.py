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


#################################### VIEWER ####################################
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

display = pl.make_display_screen_action() 
viewer = pl.make_frame_viewer( (SCREEN_WIDTH, SCREEN_HEIGHT) )
viewer.set_title("SuperPong")
viewer_actions.append( pl.make_close_viewer_action() )
viewer_actions.append( display )
viewer_actions.append( pl.make_screen_resize_action() )
get_key = act.make_get_key_action()
get_key.verbose = True
viewer_actions.append( get_key )
game_content.append( viewer )


################################### ENTITIES ###################################
# player 1 paddle
tester_paddle = act.make_rectangle( ((625, 400, 200, 100), (50, 100, 83), "paddle") )
tester_paddle.insert_action( act.make_draw_rectangle_action() )
move_player_1 = act.make_move_rectangle_action()
move_player_1.verbose = True
tester_paddle.insert_action( move_player_1 )

# player 1 controller
key_list=(K_UP, K_DOWN, K_RIGHT, K_LEFT) 
player_controller = act.make_player_controller_action( key_list, 10 )
player_controller.children.append( move_player_1 )
get_key.children.append( player_controller )

tester_paddle.insert_action( player_controller )


display.insert_entity( tester_paddle )
game_content.append( tester_paddle )
 

################################ APPEND CONTENT ################################
# add actions to viewer
for action in viewer_actions:
  viewer.insert_action( action )
  print( f"Loading {action.name} into viewer..." )
  
# append all game content
print( f"Loading game content..." )

# append all display items
print( f"Loading items into display..." )


################################# GAME LOOPER ##################################
# make the game loop & loop
looper = pl.make_game_looper( game_content )
looper.loop()
