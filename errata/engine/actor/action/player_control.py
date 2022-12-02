# action that filters key input & determines how a player should move

import pygame
from pygame.locals import *

class PlayerControlAction():
  def __init__(self, key_list=(K_UP, K_DOWN, K_RIGHT, K_LEFT), speed=10):
    self.types = ["display"]
    self.entity_state = None
    self.key_list = key_list
    self.up_key = key_list[0]
    self.down_key = key_list[1]
    self.right_key = key_list[2]
    self.left_key = key_list[3]
    self.speed = speed
    self.name = "player_control_action"
    self.children = []
    self.verbose = False 
    self.active = True
    return 
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    if type(data) == pygame.key.ScancodeWrapper:
      for k in self.key_list:
        if data[k]:
          return True
    return False
  
  def act(self, data):
    if self.condition_to_act( data ):
      # for each key passed, check if it's a valid key & handle
      pressed_actions = []
      direction = [0, 0]
      for k in self.key_list:
        if data[k]:
          pressed_actions.append( k )
          
      # create force list
      if self.right_key in pressed_actions:
        direction[0] = 1
      elif self.left_key in pressed_actions:
        direction[0] = -1
      elif self.up_key in pressed_actions:
        direction[1] = -1
      elif self.down_key in pressed_actions:
        direction[1] = 1
      else:
        direction = [0, 0]
      
      location = (self.entity_state.dimensions[0] + self.speed * direction[0], 
                  self.entity_state.dimensions[1] + self.speed * direction[1])
      
      # call children to react to keys
      for c in self.children:
        c.act( location )