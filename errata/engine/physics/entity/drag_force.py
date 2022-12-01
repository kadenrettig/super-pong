# KADEN RETTIG, CPSC 4160, FALL 2022
# drag force entity

class DragForce():
  def __init__(self, name="drag_force"):
    self.drag_constant = 0.1
    self.actions = [] 
    self.name = name 
    self.verbose = False 
    self.active = True 
    return 
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append( a )
    return