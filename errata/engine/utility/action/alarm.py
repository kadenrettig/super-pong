# KADEN RETTIG, CPSC 4160, FALL 2022
# action to activate an alarm after an interval of time

import random

class Alarm():
  def __init__(self, wait, audible):
    self.types = ["loop"]
    self.entity_state = None 
    self.name = "alarm_action"
    self.wait = wait
    self.audible = audible
    self.verbose = False
    self.children = []
    return 
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False 
    return True
  
  def act(self, data):
    if self.condition_to_act(data):
      
      # is the wait time set to be random?
      wait_time = self.wait
      if self.wait == -1:
        wait_time = random.randint(900, 2000)
      
      # activate alarm if applicable
      elapsed_time = self.entity_state.elapsed_time()
      if elapsed_time > wait_time:
        
        if self.verbose:
          print("alarm activated")
        
        # activate children actions
        for c in self.children:
          c.active = True
          c.act( data )
          
          if self.verbose:
            print( f"activating {c.name}" )
      
      if self.audible:
        return
      return