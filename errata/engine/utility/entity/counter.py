# KADEN RETTIG, CPSC 4160, FALL 2022
# total counter entity to keep track of a specified total

class Counter():
  def __init__(self, name):
    self.counter = 0
    self.actions = []
    self.name = name
    self.verbose = False 
    self.active = True
    return
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append(a)
    if self.verbose:
      print("inserting action " + a.name + " into " + self.name)
    return