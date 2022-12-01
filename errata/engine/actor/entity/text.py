# KADEN RETTIG, CPSC 4160, FALL 2022
# create a letter

import pygame
import sys
import os
from pygame.locals import *

class Text():
  def __init__(self, font_size=20, location=(20, 20), color=(255, 0, 0), text="t", name="text"):
    self.font_size = font_size
    self.location = location
    self.color = color
    self.text = text
    self.font = str(pygame.font.get_default_font())
    self.template = None
    self.actions = []
    self.name = name
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