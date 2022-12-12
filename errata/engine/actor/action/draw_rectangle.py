# KADEN RETTIG, CPSC 4160, FALL 2022
# action for drawing basic rectangle

import pygame
from pygame.locals import *

class DrawRectAction():
  def __init__(self):
    self.types = ["display"]
    self.children = []
    self.entity_state = None
    self.name = "draw_rectangle_action"
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
    if self.condition_to_act(data):
      self.draw(data)
      # Child actions
      for a in self.children:
        a.act(None)
        
      # if self.verbose:
      #   print(self.name + " for " + self.entity_state.name) 
    return 
  
  # render shape
  def draw(self, screen):
    pygame.draw.rect( screen, 
                      self.entity_state.color, 
                      self.entity_state.dimensions )
    return