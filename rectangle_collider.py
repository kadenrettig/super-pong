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
  
  def move(self, direction, speed):
    location = (( self.llc[0] + speed * direction[0], 
                   self.llc[1] + speed * direction[1] ), ( self.urc[0] + speed * direction[0], 
                   self.urc[1] + speed * direction[1] ) )

    self.llc = [location[0][0], location[0][1]]
    self.urc = [location[1][0], location[1][1]]
    return