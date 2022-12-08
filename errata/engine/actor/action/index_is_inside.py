# ADAM COPELAND, CPSC 4160, FALL 2022
# action to detect whether a physics-influenced 
# entity is within a rectangular area of the screen

class IndexIsInside():
  def __init__(self, index):
    self.types = ["physics"]
    self.entity_state = None 
    self.name = "is_inside_action"
    self.verbose = False 
    self.children = []
    self.index = index
    return 
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False 
    if data == None:
      return False 
    if self.inside(self.index, data):
      return True
    return False 
  
  # data is the particles
  def act(self, data):
    if self.condition_to_act( data ):
      if self.verbose:
            print( f"circle_{self.index} has been detected inside {self.name}" )
      for c in self.children:
        c.act( None )
    return
  
  def inside(self, index, data):
    if data.position[index][0] < self.entity_state.dimensions[0]:
      return False 
    if data.position[index][0] > self.entity_state.dimensions[2] + self.entity_state.dimensions[0]:
      return False 
    if data.position[index][1] < self.entity_state.dimensions[1]:
      return False 
    if data.position[index][1] > self.entity_state.dimensions[3] + self.entity_state.dimensions[1]:
      return False 
    return True