# KADEN RETTIG, CPSC 4160, FALL 2022
# action for playing a sound clip

import pygame
from pygame.locals import *

class Sound():
  def __init__(self, track_name):
    self.track_name = track_name
    self.types = ["loop"]
    self.entity_state = None
    self.name = "sound_action"
    self.active = True
    self.verbose = False
    return 
  
  # determine whether the sound should be played
  def condition_to_act(self, data):
    if self.active == False:
      return False
    return True
  
  # what the sound will do when called
  def act(self, data):
    if self.condition_to_act(data):
      
      # create & play sound
      sound = pygame.mixer.Sound( self.track_name )
      pygame.mixer.Sound.play( sound )
      
      if self.verbose:
        print( f"{self.name} is playing {self.entity_state.track_name}" )
    return 