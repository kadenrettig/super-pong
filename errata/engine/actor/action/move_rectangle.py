# action for moving basic rectangle

import pygame
from pygame.locals import *

class MoveRectangleAction():
  def __init__(self):
    self.types = ["event"]
    self.entity_state = None
    self.name = "move_rectangle_action"
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
    if type(data) == tuple:
      if len(data) == 2:
        return True
    return False 
  
  # what the rect will do when drawn
  def act(self, data):
    if self.condition_to_act( data ):
      
      # move the rectangle
      self.move( data )
      
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