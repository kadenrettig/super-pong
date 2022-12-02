# action to detect & filter user input, and toggle object active states based on input

import pygame 
from pygame.locals import *

class GetKeyAction():
  def __init__(self):
    self.types = ["event"]
    self.entity_state = None
    self.name = "get_key_action"
    self.children = []
    self.verbose = False 
    self.active = True
    return 
  
  def condition_to_act(self, event):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    elif event.type != KEYDOWN:
      return False
    return True
  
  def act(self, event):
    if self.condition_to_act(event):
      # grab the letter and filter it
      keys = pygame.key.get_pressed()
      
      # pass keys pressed to children actions
      for c in self.children:
        c.act( keys )
      
      # debugging
      if self.verbose:
        print( f"{self.name} for {self.entity_state.name}")
    return
    
  