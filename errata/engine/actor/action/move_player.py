# action for moving the player 

import pygame
from pygame.locals import *

class MovePlayerAction():
  def __init__(self, speed=2):
    self.types = ["display"]
    self.entity_state = None
    self.direction = [0, 0]
    self.speed = speed
    self.name = "move_player_action"
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
      
      # make new location
      location = ( self.entity_state.dimensions[0] + self.speed * self.direction[0], 
                   self.entity_state.dimensions[1] + self.speed * self.direction[1] )
      
      # move the player
      self.move( location )
      
      if self.verbose:
        print(f"{self.name} for {self.entity_state.name}") 
    return 
  
  # changes the location of a rect object
  def move(self, location):
    if self.verbose:
      print(f"moving {self.name} from {(self.entity_state.dimensions[0], self.entity_state.dimensions[1])} to {location}")
    
    self.entity_state.dimensions = (location[0],                      # x
                                    location[1],                      # y
                                    self.entity_state.dimensions[2],  # width
                                    self.entity_state.dimensions[3])  # height
    return