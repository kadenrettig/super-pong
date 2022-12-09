# KADEN RETTIG, CPSC 4160, FALL 2022
# game looper entity

import os
import sys
sys.path.insert(0, "./")
import pygame
from pygame.locals import *
import errata.engine.play as pl
import errata.engine.actor as act

class GameLooper():
  def __init__(self, name="game looper"):
    self.loop_content = []
    self.event_content = []
    self.display_content = []
    self.counter = 0
    self.name = name
    self.verbose = False
    self.active = True
    return
  
  def insert_entity(self, e):
    if self.verbose:
      print( f"inserting entity {e.name}" )
    for a in e.actions:
      self.insert_action( a )
    return

  def insert_action(self, a):
    # add event content
    if "event" in a.types:
      self.event_content.append( a )
      if self.verbose:
        print( "\t" + self.name + " added " + a.name + " event action" )
    # add loop content
    if "loop" in a.types:
      self.loop_content.append(  a)
      if self.verbose:
        print( "\t" + self.name + "added " + a .name + " loop action" )
    # add display content
    if "display" in a.types:
      self.display_content.append( a )
      if self.verbose:
        print( "\t" + self.name + " added " + a.name + " display action" )
    return

  def remove_action(self, a):
    # add event content
    if "event" in a.types:
      self.event_content.remove( a )
      if self.verbose:
        print( "\t" + self.name + " removed " + a.name + " event action" )
    # add loop content
    if "loop" in a.types:
      self.loop_content.remove(  a)
      if self.verbose:
        print( "\t" + self.name + "removed " + a .name + " loop action" )
    # add display content
    if "display" in a.types:
      self.display_content.remove( a )
      if self.verbose:
        print( "\t" + self.name + " removed " + a.name + " display action" )
    return
  
  # primary game loop
  def loop(self):
    #infinite looper
    while self.active:
      # track event content
      events = pygame.event.get()
      for e in events:
        for a in self.event_content:
          a.act(e)
          
      # track loop content
      for a in self.loop_content:
        a.act( None )
        
      # track display content
      for a in self.display_content:
        a.act( None )
        
      # loop debug
      if self.verbose:
        self.counter = self.counter + 1
        print( f"{self.name} counter = {self.counter}" )
    return