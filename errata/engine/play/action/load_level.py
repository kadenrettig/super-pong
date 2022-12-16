# ADAM COPELAND, CPSC 4160, FALL 2022
# Level load action

class LoadLevel():
  def __init__(self):
    self.types = []
    self.children = []
    self.entity_state = None
    self.name = "load_level_action"
    self.verbose = False
    return 

  def condition_to_act(self, event):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    return True
  
  def act(self, event):
    if self.condition_to_act:
      
      # load the level
      # calls the Level Manager's load method
      self.entity_state.load_level()
      
      # call children
      for a in self.children:
        a.act(None)
    return