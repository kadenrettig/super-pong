# KADEN RETTIG, CPSC 4160, FALL 2022
# sound entity for playing continuous background music

import pygame
from pygame.locals import *

class Track():
  def __init__(self, path, track):
    self.track = ( str(path) + str(track) )
    self.track_name = str(track)
    self.path = path
    self.actions = []
    self.name = "track"
    self.verbose = False 
    self.active = True
    return
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append(a)
    if self.verbose:
      print( "inserting action " + a.name + " into " + self.name )
    return