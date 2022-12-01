# KADEN RETTIG, CPSC 4160, FALL 2022
# action to increment an entity's counter 

class Increment():
  def __init__(self, value):
    self.value = value
    self.types = ["display"]
    self.entity_state = None 
    self.name = "increment_action"
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
      self.entity_state.counter += self.value
      
      # debugging
      if self.verbose:
        print( f"counter for {self.entity_state.name} incremented to {self.entity_state.counter}" )
      return