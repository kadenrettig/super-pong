# ADAM COPELAND, CPSC 4160, FALL 2022
# action to reset an entity's counter 

class ResetCount():
  def __init__(self, value):
    self.value = value
    self.types = []
    self.entity_state = None 
    self.name = "reset_count_action"
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
      # increment entity counter
      self.entity_state.counter = 0
      
      # debugging
      if self.verbose:
        print( f"counter for {self.entity_state.name} reset to {self.entity_state.count}." )
      return