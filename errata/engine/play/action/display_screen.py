# KADEN RETTIG, CPSC 4160, FALL 2022
# action for updating the display

import pygame
from pygame.locals import *
COLOR_BLACK = (0,0,0)

class DisplayScreen():
  def __init__(self):
    self.types = ["display"]
    self.entity_state = None 
    self.name = "display_screen_action"
    self.children = []
    self.verbose = False
    return
  
  def insert_entity(self, e):
    if self.verbose:
      print("inserting entity " + e.name)
    for a in e.actions:
      if "display" in a.types:
        self.children.append(a)
    return
  
  def insert_action(self, a):
    if "display" in a.types:
      self.children.append(a)
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False
    return True 
  
  def act(self, data):
    if self.condition_to_act(data):
      # clear the screen buffer to black
      self.entity_state.screen.fill(COLOR_BLACK)
      
      # call all actions with display action
      for a in self.children:
        if a.name != "screen_resize_action":
          a.act(self.entity_state.screen)
        else:
          a.act(data)
        
      # refresh the screen
      pygame.display.flip()
      
      # debugging
      if self.verbose:
        print(self.name + " for " + self.entity_state.name)
    return
  