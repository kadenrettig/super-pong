# KADEN RETTIG, CPSC 4160, FALL 2022
# main for whackamole game

import sys
sys.path.insert( 0, "./" )
import os
import random
import pygame
from pygame.locals import *

import errata.engine.utility as util
import errata.assets.sounds as sound
import errata.engine.actor as act 
import errata.engine.sound as sfx
import errata.engine.play as pl 
import errata.engine.ui as ui
import errata.python as py


################################### CREATION ###################################
to_instantiate = []
whackabox_actions = []
timer_actions = []
hud_actions = []


#################################### VIEWER ####################################
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

viewer = pl.make_frame_viewer( (SCREEN_WIDTH, SCREEN_HEIGHT) )
viewer.insert_action( pl.make_close_viewer_action() )
screen_resize = pl.make_screen_resize_action()
screen_resize.verbose = True
viewer.insert_action( screen_resize )
viewer.set_title( "Whackamole 2.0" )

display = pl.make_display_screen_action()
viewer.insert_action( display )
game_content = [ viewer ]


#################################### SOUND #####################################
# path for sound assets
sound_path = str( os.path.abspath(sound.__file__) )
sound_path = sound_path[:len(sound_path)-11]

# initialize mixer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

# background music
wii_bgm = sfx.make_track( sound_path, "we_shop.wav" )
wii_bgm.insert_action( sfx.make_bgm_action( -1 ) )
to_instantiate.append( wii_bgm )

# vine boom on button press
boom_sound = sfx.make_sound_action( str(sound_path) + "vine-boom.mp3" )

# sans voice on alarm
sans_voice = sfx.make_sound_action( str(sound_path) + "voice_sans.mp3")


##################################### MISC #####################################
# button move action
move = py.make_mover( (SCREEN_WIDTH, SCREEN_HEIGHT) )
screen_resize.children.append( move )

# hud message generation action
generate_message = py.make_generate_message()


#################################### TIMER #####################################
# make the timer
timer = util.make_timer()

# add increment action
total_counter = util.make_total_counter()
total_increment = util.make_increment_action( 1 )
total_counter.insert_action( total_increment )

# add start action
start = util.make_start_action()
timer_actions.append( start )

# add update action
timer_actions.append( util.make_update_action() )

# add alarm & children
alarm = util.make_alarm_action( -1, True )
alarm.children.append( start )
alarm.children.append( move )
alarm.children.append( sans_voice )
alarm.children.append( total_increment )
timer_actions.append( alarm )

# add complete timer to game content
to_instantiate.append( timer )


################################## WHACKABOX ###################################
# starts with a random location/color
rnd_location = (random.randint(0, SCREEN_WIDTH-100), 
                random.randint(0, SCREEN_HEIGHT-100))
rnd_color = (random.randint(50, 255), 
             random.randint(50, 255), 
             random.randint(50, 255))

# whackabox creation
whackabox_info = ( (rnd_location[0], 
                    rnd_location[1], 
                    100, 100), 
                    rnd_color )
whackabox = ui.make_button( whackabox_info )
whackabox.border = True
whackabox.border_thickness = 3

# button success counter 
success_counter = util.make_success_counter()
success_increment = util.make_increment_action( 1 )
success_counter.insert_action( success_increment )

# draw the whackabox action
whackabox.insert_action( ui.make_draw_rect_button_action() )

# button activation/deactivation actions
whackabox_actions.append( util.make_activate_action() )
whackabox_actions.append( util.make_deactivate_action() )

# button move action
whackabox_actions.append( move )

# button press action
button_press = ui.make_button_press_action()
button_press.children.append( boom_sound )
button_press.children.append( move )
button_press.children.append( start )
button_press.children.append( total_increment )
button_press.children.append( success_increment )
whackabox_actions.append( button_press )

# add complete whackabox to game content
to_instantiate.append( whackabox )


###################################### HUD #####################################
# hud creation
hud = ui.make_hud()

# hud counter for total whackabox appearances
# font size, location, color, text
hud_total = act.make_text( (25, 
                           (15, 15), 
                           (255, 255, 255), 
                           "Total: 0", 
                           "hud_total") )
hud_total.insert_action( act.make_draw_text_action() )
hud.children.append( hud_total )

# hud counter for total successful whacks
hud_success = act.make_text( (25, 
                             (17, 43), 
                             (255, 255, 255), 
                             "Successes: 0", 
                             "hud_success"))
hud_success.insert_action( act.make_draw_text_action() )
hud.children.append( hud_success )

# hud message generater for counters
generate_message.children.append( total_counter )
generate_message.children.append( success_counter )
hud_actions.append( generate_message )

# draw the hud action
draw_hud = ui.make_draw_hud_action()
hud_actions.append( draw_hud )

# add complete hud to game content
to_instantiate.append( hud )


################################ APPEND CONTENT ################################
# add actions to whackabox
for action in whackabox_actions:
  print(f"Loaded whackabox {action.name}...")
  whackabox.insert_action( action )
  
# add actions to timer
for action in timer_actions:
  print(f"Loaded timer {action.name}...")
  timer.insert_action( action )

# add actions to hud
for action in hud_actions:
  print(f"Loaded HUD {action.name}...")
  hud.insert_action( action )

# instantiate game content & display
for content in to_instantiate:
  print(f"Loaded game content {content.name}...")
  display.insert_entity( content )
  game_content.append( content )


################################# GAME LOOPER ##################################
# make the game loop & loop
looper = pl.make_game_looper( game_content )
looper.loop()