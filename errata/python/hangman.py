# KADEN RETTIG, CPSC 4160, FALL 2022
# main for hangman game

import sys
import os
sys.path.insert(0,"./")
import random

from pygame.locals import *
import errata.engine.play as pl 
import errata.engine.actor as act

##### WORD & LETTERS #####

from english_words import english_words_lower_alpha_set
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_content = []     # list of Letter objects to be displayed
alphabet_content = [] # stores a letter object for each letter of the alphabet
WORD_LEFT = 200       # the x-coordinate of the first displayed letter  
pspace = 0            # "personal space" for each letter

# loop until appropriate word found
while True:
  WORD = random.choice( tuple(english_words_lower_alpha_set) )
  
  if len( WORD ) > 4 and len( WORD ) < 9:
    break

# create letter objects for each character & add them to a list
for l in WORD:
  letter_info = ( 55, (WORD_LEFT+pspace, 600), (255, 255, 255), str(l), str(l)+"_letter" )
  letter = act.make_text( letter_info )
  letter.insert_action( act.make_draw_text_action() )
  word_content.append( letter )
  pspace += 75

for l in alphabet:
  letter_info = ( 35, (0, 0), (255, 255, 255), str(l), str(l)+"_alphabet" )
  letter = act.make_text( letter_info )
  letter.insert_action( act.make_draw_text_action() )
  alphabet_content.append( letter )

print(WORD)

##### LETTER BOXES #####

pspace = 0
box_content = []  # stores each rect object for each letter

for b in WORD:
  box_info = ( (WORD_LEFT+pspace, 600, 60, 60), (150, 255, 150), str(b)+"_letterbox" )
  box = act.make_rectangle( box_info )
  box.insert_action( act.make_draw_rectangle_action() )
  box_content.append( box )
  pspace += 75
  
##### VIEWER #####

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

viewer = pl.make_frame_viewer( (SCREEN_WIDTH, SCREEN_HEIGHT) )
viewer.insert_action( pl.make_close_viewer_action() )
detect_letter = act.make_guess_letter_action( WORD )
detect_letter.verbose = True
viewer.insert_action( detect_letter )
viewer.set_title( "Hangman" )

display = pl.make_display_screen_action()
viewer.insert_action( display )
game_content = [ viewer ]

##### WIN/LOSE SCREEN TEXT #####

result_text = []  # stores the objects that display the win/lose screen

win_info = ( 70, (SCREEN_WIDTH/2-250, SCREEN_HEIGHT/2-25), 
            (255, 255, 255), "YOU WON :)", "win_text" )
win_text = act.make_text( win_info )
win_text.insert_action( act.make_draw_text_action() )
result_text.append( win_text )

lose_info = ( 70, (SCREEN_WIDTH/2-250, SCREEN_HEIGHT/2-25), 
             (255, 255, 255), "YOU LOST :(", "lose_text" )
lose_text = act.make_text( lose_info )
lose_text.insert_action( act.make_draw_text_action() )
result_text.append( lose_text )

##### HANGMAN FRAME #####

FRAME_COLOR = ( (150, 50, 50) )

# make hangman frame rect
hangman_frame_info = ( (250, 500, 124, 10), FRAME_COLOR, "frame_rect" )
hangman_frame_rect= act.make_rectangle( hangman_frame_info )
hangman_frame_rect.insert_action( act.make_draw_rectangle_action() )
display.insert_entity( hangman_frame_rect )
game_content.append( hangman_frame_rect )

# make hangman pole length rect
hangman_pole_length_info = ( (305, 110, 10, 390), FRAME_COLOR, "pole_length_rect" )
hangman_pole_length_rect = act.make_rectangle( hangman_pole_length_info )
hangman_pole_length_rect.insert_action( act.make_draw_rectangle_action() )
display.insert_entity( hangman_pole_length_rect )
game_content.append( hangman_pole_length_rect )

# make hangman pole top rect
hangman_pole_top_info = ( (275, 110, 250, 10), FRAME_COLOR, "pole_top_rect" )
hangman_pole_top_rect = act.make_rectangle( hangman_pole_top_info )
hangman_pole_top_rect.insert_action( act.make_draw_rectangle_action() )
display.insert_entity( hangman_pole_top_rect )
game_content.append( hangman_pole_length_rect )

##### HANGMAN ROPE #####

ROPE_COLOR = ((130, 100, 65))

# make hangman rope rect
rope_info = ( (515, 120, 5, 50), ROPE_COLOR, "rope_rect" )
rope_rect = act.make_rectangle( rope_info )
rope_rect.insert_action( act.make_draw_rectangle_action() )
display.insert_entity( rope_rect )
game_content.append( rope_rect )

##### HUNG MAN/WOMAN #####

PERSON_COLOR = ( (100, 240, 200) )
person_parts = []

# make person head
person_head_info = ( (30), (518, 185), PERSON_COLOR, "person_part_1" )
person_head_circ = act.make_circle( person_head_info )
person_head_circ.insert_action( act.make_draw_circle_action() )
person_parts.append( person_head_circ )

# make person body
person_body_info = ( (507, 210, 25, 85), PERSON_COLOR, "person_part_2" )
person_body_rect = act.make_rectangle( person_body_info )
person_body_rect.insert_action( act.make_draw_rectangle_action() )
person_parts.append( person_body_rect )

# make person left arm
person_arm1_info = ( (455, 230, 55, 12), PERSON_COLOR, "person_part_3" )
person_arm1_rect = act.make_rectangle( person_arm1_info )
person_arm1_rect.insert_action( act.make_draw_rectangle_action() )
person_parts.append( person_arm1_rect )

# make person right arm
person_arm2_info = ( (530, 230, 55, 12), PERSON_COLOR, "person_part_4" )
person_arm2_rect = act.make_rectangle( person_arm2_info )
person_arm2_rect.insert_action( act.make_draw_rectangle_action() )
person_parts.append( person_arm2_rect )

# make person pelvis
person_pel_info = ( (490, 285, 60, 10), PERSON_COLOR, "person_part_5" )
person_pel_rect = act.make_rectangle( person_pel_info )
person_pel_rect.insert_action( act.make_draw_rectangle_action() )
person_parts.append( person_pel_rect )

# make person left leg
person_leg1_info = ( (490, 295, 15, 50), PERSON_COLOR, "person_part_6" )
person_leg1_rect = act.make_rectangle( person_leg1_info )
person_leg1_rect.insert_action( act.make_draw_rectangle_action() )
person_parts.append( person_leg1_rect )

# make person right leg
person_leg2_info = ( (535, 295, 15, 50), PERSON_COLOR, "person_part_7" )
person_leg2_rect = act.make_rectangle( person_leg2_info )
person_leg2_rect.insert_action( act.make_draw_rectangle_action() )
person_parts.append( person_leg2_rect )

##### INSERT ENTITIES AND APPEND TO DISPLAY #####

# add each part of the hangman
for p in person_parts:
  p.active = False
  display.insert_entity( p ) 
  game_content.append( p )
  
# add each letter object
for l in word_content:
  l.active = False
  display.insert_entity( l )
  game_content.append( l )
  
# add each letter box object
for b in box_content:
  b.active = True 
  display.insert_entity( b )
  game_content.append( b )
  
# add each alphabet letter
for a in alphabet_content:
  a.active = False
  display.insert_entity( a )
  game_content.append( a )
  
# add the win/lose text
for t in result_text:
  t.active = False 
  display.insert_entity( t )
  game_content.append( t )

##### LOOPER #####

game_looper = pl.make_game_looper( game_content )
game_looper.loop()

