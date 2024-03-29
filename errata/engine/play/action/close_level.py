# ADAM COPELAND, CPSC 4160, FALL 2022
# Level close action

class CloseLevel():
  def __init__(self):
    self.types = []
    self.children = []
    self.entity_state = None
    self.name = "close_level_action"
    self.verbose = False
    return 
  
  def act(self, data):
    print("closing level...")
    
    # close the level, 
    # calls the Level Manager's close method
    self.entity_state.close_level()
    
    # Run children
    for a in self.children:
      a.act(None)
    return