# KADEN RETTIG, CPSC 4160, FALL 2022
# action to resize the window on user interaction

import pygame
from pygame.locals import *

class ScreenResize():
  def __init__(self):
    self.types = ["display"]
    self.entity_state = None
    self.name = "screen_resize"
    self.children = []
    self.verbose = False
    return
    
  def condition_to_act(self, event):
    if event == None:
      return False
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    if event.type == VIDEORESIZE:
      return True 
    return False
  
  def act(self, event):
    if self.condition_to_act(event):
      self.entity_state.set_mode( event.size, 
                                  self.entity_state.mode, 
                                  self.entity_state.depth )
      for d in self.children:
        d.bounds = ( 0, 0, 
                     self.entity_state.dimensions[0], 
                     self.entity_state.dimensions[1] )
        if self.verbose:
          print(f"{d.name} bounds set to ({self.entity_state.dimensions[0]}, {self.entity_state.dimensions[1]})")
    return