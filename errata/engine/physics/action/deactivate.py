# KADEN RETTIG, CPSC 4160, FALL 2022
# action to deactivate the 'active' state of particle(s)

class Deactivate():
  def __init__(self):
    self.types = ["display"]
    self.entity_state = None 
    self.name = "deactivate_action"
    self.active = False
    self.verbose = False
    self.children = []
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
      # deactivate all particle indexes
      for i in data:
        self.entity_state.active_particle[i] = False 
      
      if self.verbose:
        print( f"{self.name} is deactivating {self.entity_state.name}" )
      
      # deactivate children
      for c in self.children:
        c.active = False
        
        # debugging
        if self.verbose:
          print( f"{self.name} is deactivating {c.name}" )
          
      # deactivate self until next call
      self.active = False
      return