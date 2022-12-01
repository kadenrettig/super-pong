# KADEN RETTIG, CPSC 4160, FALL 2022
# action for drawing basic letter

import pygame
from pygame.locals import *

class DrawTextAction():
  def __init__(self):
    self.types = ["display"]
    self.entity_state = None
    self.name = "draw_text_action"
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
    if self.condition_to_act(data):
      self.draw(data)
      if self.verbose:
        print(self.name + " for " + self.entity_state.name)
    return
  
  # render shape
  def draw(self, screen):
    font = pygame.font.Font(self.entity_state.font, self.entity_state.font_size)
    text = font.render(str(self.entity_state.text), 
                       True, 
                       self.entity_state.color)
    screen.blit(text, self.entity_state.location)
    
  # update 
