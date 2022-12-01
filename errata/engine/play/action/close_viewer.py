# KADEN RETTIG, CPSC 4160, FALL 2022
# detect quit action

from pygame.locals import *

class CloseViewer():
  def __init__(self):
    self.types = ["event"]
    self.entity_state = None
    self.name = "detect_quit_action"
    self.verbose = False
    return 
  
  def condition_to_act(self, event):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    if event.type == QUIT:
      return True
    elif event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        print("closing game...")
        return True
    return False
  
  def act(self, event):
    if self.condition_to_act(event):
      # terminate the display (action in frame viewer)
      self.entity_state.terminate()

      if self.verbose:
        print(f"{self.name} has terminated {self.entity_state.name}")
      
      # debugging
      if self.verbose:
        print(self.name + " for " + self.entity_state.name)
    return