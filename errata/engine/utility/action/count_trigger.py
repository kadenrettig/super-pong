# ADAM COPELAND, CPSC 4160, FALL 2022
# Action causes children to act when score reached the given value

class CountTrigger():
  def __init__(self, value):
    self.value = value
    self.types = []
    self.entity_state = None 
    self.name = "reset_count_action"
    self.verbose = True
    self.children = []
    return 
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False 
    if self.entity_state.counter == self.value:
      return True
    return False
  
  def act(self, data):
    if self.condition_to_act(data):
      # Run child actions
      for c in self.children:
          c.act( data )
      
      # debugging
      if self.verbose:
        print( f"counter for {self.entity_state.name} reached {self.value}." )
      return