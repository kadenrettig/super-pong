# KADEN RETTIG, CPSC 4160, FALL 2022
# rectangular collider entity for collision simulation

class RectangleCollider():
  def __init__(self, llc = [0.0, 0.0], urc = [100.0, 100.0], name="rectangle_collider"):
    self.llc = llc 
    self.urc = urc 
    self.actions = []
    self.name = name 
    self.verbose = False 
    self.active = True 
    return 
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append( a )
    return
  
  def move(self, info):
    return