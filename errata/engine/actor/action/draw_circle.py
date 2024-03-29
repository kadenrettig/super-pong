# KADEN RETTIG, CPSC 4160, FALL 2022
# action for drawing basic circle

import pygame
from pygame.locals import *

class DrawCircleAction():
  def __init__(self):
    self.types = ["display"]
    self.entity_state = None
    self.name = "draw_circle_action"
    self.verbose = False
    return 
  
  # determine whether the circle should be rendered
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    if data == None:
      return False
    return True
  
  # what the circle will do when drawn
  def act(self, data):
    if self.condition_to_act(data):
      self.draw(data)
      if self.verbose:
        print(self.name + " for " + self.entity_state.name)
    return 
  
  # render shape
  def draw(self, screen):
    pygame.draw.circle(screen, 
                       self.entity_state.color, 
                       self.entity_state.location, 
                       self.entity_state.radius, 
                       self.entity_state.thickness)
    return