# KADEN RETTIG, CPSC 4160, FALL 2022
# action for drawing the hud

import pygame 

class DrawHUD():
  def __init__(self):
    self.types = ["display"]
    self.entity_state = None 
    self.verbose = False 
    self.children = []
    self.name = "draw_hud_action"
    return 
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False 
    if data == None:
      return False 
    return True
  
  def act(self, data):
    if self.condition_to_act(data):
      self.draw(data)
      if self.verbose:
        print( self.name + " for " + self.entity_state.name )
    return
  
  def draw(self, data):
    for c in self.entity_state.children:
      for a in c.actions:
        a.act(data)
        
        if self.verbose:
          print(f"calling act of {a.name} from {self.name}")
    return