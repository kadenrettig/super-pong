# action to detect & filter user input, and toggle object active states based on input

import pygame 
from pygame.locals import *

class PlayerController():
  def __init__(self, key_list=(K_UP, K_DOWN, K_RIGHT, K_LEFT)):
    self.types = ["event"]
    self.entity_state = None
    self.up_key = key_list[0]
    self.down_key = key_list[1]
    self.right_key = key_list[2]
    self.left_key = key_list[3]
    self.name = "player_controller_action"
    self.children = []
    self.verbose = False 
    self.active = True
    self.direction = [0,0]
    return 
  
  def condition_to_act(self, event):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    if event.type != KEYDOWN:
      if event.type != KEYUP:
        return False
    return True
  
  def act(self, event):
    if self.condition_to_act( event ):
      
      if event.type == pygame.KEYDOWN:
        if self.up_key != None and event.key == self.up_key:
          self.direction[1] += -1
        elif self.down_key != None and event.key == self.down_key:
          self.direction[1] += 1
        elif self.left_key != None and event.key == self.left_key:
          self.direction[0] += -1
        elif self.right_key != None and event.key == self.right_key:
          self.direction[0] += 1
          
      if event.type == pygame.KEYUP:
        if self.up_key != None and event.key == self.up_key:
          self.direction[1] += 1
        if self.down_key != None and event.key == self.down_key:
          self.direction[1] += -1
        if self.left_key != None and event.key == self.left_key:
          self.direction = [0, 0]
        if self.right_key != None and event.key == self.right_key:
          self.direction = [0, 0]
    
      # pass new location to children
      for c in self.children:
        c.act( self.direction )
      
      # debugging
      if self.verbose:
        print( f"{self.name} for {self.entity_state.name}")
    return
    
  