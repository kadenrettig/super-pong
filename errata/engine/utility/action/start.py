# KADEN RETTIG, CPSC 4160, FALL 2022
# action to increment corresponding timer

import time

class Start():
  def __init__(self):
    self.types = ["loop"]
    self.entity_state = None 
    self.name = "start_action"
    self.verbose = False
    self.active = False
    self.children = []
    return 
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False 
    if self.active == False:
      return False
    return True
  
  def act(self, data):
    if self.condition_to_act(data):
      # increment entity counter
      self.entity_state.start_time = int(round(time.time() * 1000))
      
      # debugging
      if self.verbose:
        print( f"start_time is now {self.entity_state.start_time}" )
      
      # become inactive until called again
      self.active = False
      return