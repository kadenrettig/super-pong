# KADEN RETTIG, CPSC 4160, FALL 2022
# action for moving the player 

import pygame
from pygame.locals import *
import errata.engine.physics as phys

class MovePlayerAction():
  def __init__(self, speed=2, max_width=1280, max_height=720):
    self.types = ["display"]
    self.entity_state = None
    self.direction = [0, 0]
    self.speed = speed
    self.max_width = max_width
    self.max_height = max_height
    self.name = "move_player_action"
    self.children = []
    self.verbose = False
    return 
  
  # determine whether the rectangle should be rendered
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False
    if data == None:
      return False
    return True 
  
  # what the rect will do when drawn
  def act(self, data):
    if self.condition_to_act( data ):
      
      # if a new direction is received, update it
      if type(data) == list:
        if len(data) == 2:
          self.direction = data

      # pass the direction & speed to the entities associated with the player
      for c in self.children:
        c.move(self.direction, self.speed, self.max_width, self.max_height)

      if self.verbose:
        print(f"{self.name} for {self.entity_state.name}") 
    return 