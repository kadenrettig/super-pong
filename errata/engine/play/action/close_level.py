# ADAM COPELAND, CPSC 4160, FALL 2022
# Level load action

class CloseLevel():
  def __init__(self):
    self.types = ["event"]
    self.entity_state = None
    self.name = "detect_quit_action"
    self.verbose = False
    return 
  
  def act(self, event):
    print("loading level...")
    self.entity_state.close_level()
    return