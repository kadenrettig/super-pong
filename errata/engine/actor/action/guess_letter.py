# KADEN RETTIG, CPSC 4160, FALL 2022
# action to detect & filter user input, and toggle object active states based on input

import sys
import os
sys.path.insert(0,"./")

import pygame 
from pygame.locals import *

import errata.engine.actor as act


class GuessLetterAction():
  def __init__(self, word):
    self.types = ["event"]
    self.entity_state = None
    self.name = "detect_letter_action"
    self.verbose = False 
    self.active = True
    self.word = word
    self.wrong_guesses = []
    self.correct_guesses = []
    self.content_left = 100
    self.max_guesses = 7
    return 
  
  def condition_to_act(self, event):
    if self.entity_state == None:
      print("entity state None")
      return False
    if self.entity_state.active == False:
      return False
    # filter all events as KEYDOWN, otherwise ignore
    # prevents unnecessary calling of get_letter()
    elif event.type != KEYDOWN:
      return False
    return True
  
  def act(self, event):
    if self.condition_to_act(event):
      # grab the letter and filter it
      self.get_letter(event)
      
      # draw all of the necessary letters, boxes, and hangman parts
      self.draw()
      
      # debugging
      if self.verbose:
        print(self.name + " for " + self.entity_state.name)
        
      ## CHECK FOR WIN
      # calculate number of correct letters, accounting for duplicates
      total = 0     # tracks num of correct letters
      for c in self.correct_guesses:
        for w in self.word:
          if c == w:
            total += 1
      # determine win condition
      if total == len(self.word): 
        self.end_screen("win_text")
        print("YOU WON :)")
        
      ## CHECK FOR LOSS
      elif len(self.wrong_guesses) >= self.max_guesses:
        self.end_screen("lose_text")
        print("YOU LOST :(")
    return

  # draw the letters and parts of hangman
  def draw(self):
    # for every letter in the word, check whether or not to display it
    for letter in self.word:
      # if the letter is correct, display it & undraw the box for the letter
      if letter in self.correct_guesses:
        self.toggle_active( str(letter)+"_letter", True )
        self.toggle_active( str(letter)+"_letterbox", False )
        
    # for every wrongly guessed letter, add a part to the hangman
    for i in range(1, len(self.wrong_guesses)+1):
      self.toggle_active("person_part_"+str(i), True)
    
    # for every wrongly guessed letter, add that letter to the screen
    for letter in self.wrong_guesses:
      index = self.wrong_guesses.index( letter )
      x = 950 + (50 * index)
      y = 200
      new_location = ( x, y )
      self.add_wrong_letter( str(letter)+"_alphabet", new_location )
      self.toggle_active( str(letter)+"_alphabet", True )
    return
  
  # toggle end screen (win OR lose)
  def end_screen(self, result):
    for action in self.entity_state.actions:
          if action.name == "display_screen_action":
            for entity_action in action.children:
              # disable all actions except terminate and letter drawing
              if entity_action.name != "detect_quit_action" or "draw_letter_action":
                entity_action.active = False
              # disable all things drawn to the screen except the end screen
              if entity_action.entity_state.name != result:
                entity_action.entity_state.active = False
    self.toggle_active( result, True )
    return
  
  # move letter to specified location for list of wrong guesses
  def add_wrong_letter(self, name, location):
    for action in self.entity_state.actions:            # for each action in the frame viewer
      if action.name == "display_screen_action":        # find the display action
        for entity_action in action.children:           # loop through display's children
          if entity_action.entity_state.name == name:   # find the requested object
            entity_action.entity_state.move( location )
    return
  
  # toggle an entity's active attribute to off | AKA the skeleton key
  def toggle_active(self, name, status):
    for action in self.entity_state.actions:            # for each action in the frame viewer
      if action.name == "display_screen_action":        # find the display action
        for entity_action in action.children:           # loop through display's children
          if entity_action.entity_state.name == name:   # find the requested object
            entity_action.entity_state.active = status  # toggle it
    return
  
  # decide whether the entered letter was correct or not & add to corresponding list
  def right_or_wrong(self, letter):
    letter = str.lower(letter)
    for char in self.word:                              # for every letter in the word
      if char == letter:                                # if the letter is the same as the one inputted
        if letter not in self.correct_guesses:          # count it as a correct letter
          self.correct_guesses.append( letter )
        print( "correct guess: " + letter )
    if letter not in self.correct_guesses:              # else count it as a wrong letter
      if letter not in self.wrong_guesses:
        self.wrong_guesses.append( letter )
      print("wrong guess: " + letter)
    return
  
  ## GET USER INPUT
  # manually created to prevent user from pushing any buttons but alphas
  def get_letter(self, event):
    if event.key == K_q:
      self.right_or_wrong("Q")
      if self.verbose:
        print("Key Q pressed")
    elif event.key == K_w:
      self.right_or_wrong("W")
      if self.verbose:
        print("Key W pressed")
    elif event.key == K_e:
      self.right_or_wrong("E")
      if self.verbose:
        print("Key E pressed")
    elif event.key == K_r:
      self.right_or_wrong("R")
      if self.verbose:
        print("Key R pressed")
    elif event.key == K_t:
      self.right_or_wrong("T")
      if self.verbose:
        print("Key T pressed")
    elif event.key == K_y:
      self.right_or_wrong("Y")
      if self.verbose:
        print("Key Y pressed")
    elif event.key == K_u:
      self.right_or_wrong("U")
      if self.verbose:
        print("Key U pressed")
    elif event.key == K_i:
      self.right_or_wrong("I")
      if self.verbose:
        print("Key I pressed")
    elif event.key == K_o:
      self.right_or_wrong("O")
      if self.verbose:
        print("Key O pressed")
    elif event.key == K_p:
      self.right_or_wrong("P")
      if self.verbose:
        print("Key P pressed")
    elif event.key == K_a:
      self.right_or_wrong("A")
      if self.verbose:
        print("Key A pressed")
    elif event.key == K_s:
      self.right_or_wrong("S")
      if self.verbose:
        print("Key S pressed")
    elif event.key == K_d:
      self.right_or_wrong("D")
      if self.verbose:
        print("Key D pressed")
    elif event.key == K_f:
      self.right_or_wrong("F")
      if self.verbose:
        print("Key F pressed")
    elif event.key == K_g:
      self.right_or_wrong("G")
      if self.verbose:
        print("Key G pressed")
    elif event.key == K_h:
      self.right_or_wrong("H")
      if self.verbose:
        print("Key H pressed")
    elif event.key == K_j:
      self.right_or_wrong("J")
      if self.verbose:
        print("Key J pressed")
    elif event.key == K_k:
      self.right_or_wrong("K")
      if self.verbose:
        print("Key K pressed")
    elif event.key == K_l:
      self.right_or_wrong("L")
      if self.verbose:
        print("Key L pressed")
    elif event.key == K_z:
      self.right_or_wrong("Z")
      if self.verbose:
        print("Key Z pressed")
    elif event.key == K_x:
      self.right_or_wrong("X")
      if self.verbose:
        print("Key X pressed")
    elif event.key == K_c:
      self.right_or_wrong("C")
      if self.verbose:
        print("Key C pressed")
    elif event.key == K_v:
      self.right_or_wrong("V")
      if self.verbose:
        print("Key V pressed")
    elif event.key == K_b:
      self.right_or_wrong("B")
      if self.verbose:
        print("Key B pressed")
    elif event.key == K_n:
      self.right_or_wrong("N")
      if self.verbose:
        print("Key N pressed")
    elif event.key == K_m:
      self.right_or_wrong("M")
      if self.verbose:
        print("Key M pressed")
    return