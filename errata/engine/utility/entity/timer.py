# KADEN RETTIG, CPSC 4160, FALL 2022
# timer entity to keep track of game time, etc.

import time

class Timer():
  def __init__(self):
    self.start_time = int(round(time.time() * 1000))
    self.current_time = int(round(time.time() * 1000))
    self.actions = []
    self.name = "timer"
    self.verbose = False 
    self.active = True
    return
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append(a)
    if self.verbose:
      print("inserting action " + a.name + " into " + self.name)
    return
  
  # updates the class variable storing the current time
  def tick(self):
    self.current_time = int(round(time.time() * 1000))
    if self.verbose:
      print("updated current time")
      
  # returns elapsed time with start & current times
  def elapsed_time(self):
    # take the difference between start & current times
    elapsed_time = self.current_time - self.start_time
    if self.verbose:
      print("updated elapsed time")
    return elapsed_time