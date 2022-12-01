# KADEN RETTIG, CPSC 4160, FALL 2022
# create a circle

import pygame
import sys
import os
from pygame.locals import *

class Circle():
  def __init__(self, radius=20, location=(30, 30), color=(0, 255, 0), name="circle"):
    self.radius = radius
    self.location = location
    self.color = color
    self.thickness = 0
    self.template = None
    self.actions = []
    self.name = name
    self.verbose = False 
    self.active = True
    return
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append( a )
    if self.verbose:
      print( f"inserting action {a.name} into {self.name}" )
    return
  
  # changes the location of a letter/text object
  def move(self, location):
    if self.verbose:
      print( f"moving {self.name} from {self.location} to {location}" )
    self.location = location
    return