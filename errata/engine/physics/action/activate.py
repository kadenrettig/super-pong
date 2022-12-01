# KADEN RETTIG, CPSC 4160, FALL 2022
# action to activate the 'active' state of particle(s)

class Activate():
  def __init__(self):
    self.types = ["display"]
    self.entity_state = None 
    self.name = "activate_action"
    self.active = False
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
      # activate all particles
      for i in range( 0, len(self.entity_state.active_particle)):
        self.entity_state.active_particle[i] = True 
      
      if self.verbose:
        print( f"{self.name} is activating {self.entity_state.name}" )
      
      # activate children
      for c in self.children:
        c.active = True
        
        # debugging
        if self.verbose:
          print( self.name + " is activating " + c.name )
          
      # disable self until called next
      self.active = False
      return