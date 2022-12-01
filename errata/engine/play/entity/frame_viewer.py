# KADEN RETTIG, CPSC 4160, FALL 2022
# frame viewer

import pygame
from pygame.locals import *

class FrameViewer():
  def __init__(self,  dimensions=[1280, 720], mode=RESIZABLE | DOUBLEBUF, depth=32, title="Errata Window", name="frame_viewer"):
    pygame.init()
    self.screen = pygame.display.set_mode(dimensions, mode, depth)
    self.dimensions = dimensions
    self.mode = mode
    self.depth = depth
    self.title = title
    self.actions = []
    self.name = name
    self.verbose = False
    self.active = True
    return 

  def insert_action(self, a):
    a.entity_state = self
    self.actions.append(a)
    return
  
  # terminates the game window, exits pygame, and quits python
  def terminate(self):
    # import exit to exit python
    from sys import exit 
    if self.verbose:
      print(self.name + " terminating")
    pygame.quit()
    exit()
  
  # set the title of the window
  def set_title(self, title):
    self.title = title
    pygame.display.set_caption(title)
    if self.verbose:
      print(self.name + " titled changed to = " + title)
    return
  
  # set the mode of the frame viewer
  def set_mode(self, ssize, mode, depth):
    self.screen = pygame.display.set_mode(ssize, mode, depth)
    self.dimensions = [ssize[0], ssize[1]]
    self.mode = mode 
    self.depth = depth 
    if self.verbose:
      print(self.name + " new size = " + str(self.dimensions))
    return