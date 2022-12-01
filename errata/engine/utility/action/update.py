# KADEN RETTIG, CPSC 4160, FALL 2022
# action to update the start time of an entity

class Update():
  def __init__(self):
    self.types = ["loop"]
    self.entity_state = None 
    self.name = "update_action"
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
      # update current time
      self.entity_state.tick()
      
      # debugging
      if self.verbose:
        print( f"current_time is now {self.entity_state.current_time}" )
      return