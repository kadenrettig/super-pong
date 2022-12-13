# KADEN RETTIG, CPSC 4160, FALL 2022
# create an image to be displayed

import pygame
import sys
import os
from pygame.locals import *

class Image():
  def __init__(self, location=(20, 20), size=(40, 15), image_name="default.jpg", name="image"):
    self.location = location
    self.size = size
    self.image_name = image_name
    self.template = None
    self.name = name
    self.actions = []
    self.verbose = False 
    self.active = True
    return
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append(a)
    return
  
  # used to add a wrong letter to the display
  # changes the location of a letter/text object
  def move(self, location):
    if self.verbose:
      print("moving " + self.name + " from " + self.location + " to " + location)
    self.location = location
    return