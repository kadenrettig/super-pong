# KADEN RETTIG, CPSC 4160, FALL 2022
# action for drawing an image to the screen

import os
import errata.assets.textures as textures

import pygame
from pygame.locals import *

class DrawImageAction():
  def __init__(self):
    self.types = ["display"]
    self.entity_state = None
    self.name = "draw_image_action"
    self.verbose = False
    return 
  
  # determine whether the text should be rendered
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    if data == None:
      return False 
    return True 
  
  # what the text will do when drawn
  def act(self, data):
    if self.condition_to_act( data ):
      
      self.draw( data )
      if self.verbose:
        print(self.name + " for " + self.entity_state.name)
    return
  
  # render shape
  def draw(self, screen):
    
    # determine where the image is located
    image_path = str( os.path.abspath(textures.__file__) )
    image_path = image_path[:len(image_path)-11]
    
    # create image & resize
    image = pygame.image.load( image_path + self.entity_state.image_name ).convert_alpha()
    sized_image = pygame.transform.smoothscale( image, self.entity_state.size )
    
    # draw the image
    screen.blit( sized_image, self.entity_state.location )
    return
