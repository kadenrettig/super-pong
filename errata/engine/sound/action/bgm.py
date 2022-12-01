# KADEN RETTIG, CPSC 4160, FALL 2022
# action for playing bgm

import pygame
from pygame.locals import *

class BGM():
  def __init__(self, duration):
    self.duration = duration
    self.types = ["loop"]
    self.entity_state = None
    self.name = "bgm_action"
    self.active = True
    self.verbose = False
    return 
  
  # determine whether the sound should be played
  def condition_to_act(self, data):
    if self.entity_state == None:
      print("entity state none")
      return False
    if self.entity_state.active == False:
      print("entity state not active")
      return False
    if self.active == False:
      return False
    return True
  
  # what the sound will do when called
  def act(self, data):
    if self.condition_to_act(data):
      
      # get that music playing!!
      self.load()
      self.play()
      
      # if the track is set to play continuously, don't reactivate
      if self.duration == -1:
        self.active = False
      
      if self.verbose:
        print( f"{self.name} is playing {self.entity_state.track_name} for {self.duration} seconds" )
    return 
  
  # load the track
  def load(self):
    pygame.mixer.music.load( self.entity_state.track )
    if self.verbose:
      print(f"loading track {self.entity_state.track_name}")
    return
  
  # play the track
  def play(self):
    pygame.mixer.music.play( self.duration )
    if self.verbose:
      print(f"playing track {self.entity_state.track}")
    return
  
  # stop the track
  def stop(self):
    pygame.mixer.music.stop()
    if self.verbose:
      print(f"stopped {self.entity_state.track_name} playback")