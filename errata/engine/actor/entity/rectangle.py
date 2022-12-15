# KADEN RETTIG, STEPHEN SAMS (added move()), CPSC 4160, FALL 2022
# create a rectangle

import pygame
import sys
import os
from pygame.locals import *

class Rectangle():
  def __init__(self, dimensions=(30, 30, 60, 60), color=(0, 255, 0), name="rectangle"):
    self.dimensions = dimensions
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
    self.actions.append(a)
    if self.verbose:
      print("inserting action " + a.name + " into " + self.name)
    return

  # changes the location of a rect object using a given speed and direction
  # utilized by the move_player action
  def move(self, direction, speed, max_width, max_height):

    # calculate the new position to be moved to
    location = [ self.dimensions[0] + speed * direction[0], 
                 self.dimensions[1] + speed * direction[1] ]
    
    # ensure the new location isn't out of the screen bounds
    if location[0] + self.dimensions[2] > max_width:
      location[0] = max_width - self.dimensions[2]
    elif location[0] < 0:
      location[0] = 0
    if location[1] + self.dimensions[3] > max_height:
      location[1] = max_height - self.dimensions[3]
    elif location[1] < 0:
      location[1] = 0
    
    # assign the new location to the rect's variables
    self.dimensions = ( location[0],                      # x
                        location[1],                      # y
                        self.dimensions[2],               # width
                        self.dimensions[3] )              # height
    
    if self.verbose:
      print(f"moving {self.name} from {(self.dimensions[0], self.dimensions[1])} to {location}")
    return
