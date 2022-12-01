# KADEN RETTIG, CPSC 4160, FALL 2022
# force entity

class GravityForce():
  def __init__(self, name="gravity_force"):
    self.gravity = [0.0, -1.0]
    self.actions = []
    self.name = name
    self.verbose = False 
    self.active = True 
    return 
  
  def insert_action(self, a):
    a.entity_state = self
    self.actions.append( a )
    return