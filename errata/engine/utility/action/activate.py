# KADEN RETTIG, CPSC 4160, FALL 2022
# action to activate the 'active' state of an entity

class Activate():
  def __init__(self):
    self.types = []
    self.entity_state = None 
    self.name = "activate_action"
    self.active = True
    self.verbose = False
    self.children = []
    return
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False
    if self.entity_state.active == True:
      return False
    if self.active == False:
      return False
    return True
  
  def act(self, data):
    if self.condition_to_act(data):
      
      # activate entity
      self.entity_state.active = True
      
      if self.verbose:
        print( f"{self.name} is activating {self.entity_state.name}" )
      
      # activate children
      for c in self.children:
        c.active = True
        
        # debugging
        if self.verbose:
          print( self.name + " is activating " + c.name )
      return