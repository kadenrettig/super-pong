# KADEN RETTIG, CPSC 4160, FALL 2022
# action to detect a button press

from pygame.locals import * 

class ButtonPress():
  def __init__(self):
    self.types = ["event"]
    self.entity_state = None 
    self.name = "button_pressed_action"
    self.verbose = False
    self.children = [] 
    return 
  
  def condition_to_act(self, event):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False
    if event.type == MOUSEBUTTONDOWN:
      # is the mouse button down?
      pos = event.pos 
      return self.entity_state.hover(pos)
    return False
  
  def act(self, event):
    if self.condition_to_act(event):
      
      # activate children
      for c in self.children:
        if self.verbose:
          print( self.name + " is acting for " + c.name )
        c.active = True
        c.act(event)
        
      # debugging
      if self.verbose:
        print( self.name 
               + " for " 
               + self.entity_state.name 
               + " at " 
               + str( event.pos ))
    return