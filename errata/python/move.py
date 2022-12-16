# KADEN RETTIG, CPSC 4160, FALL 2022
# specific to this game: move the button to a random position

import random

class Move():
  def __init__(self, bounds):
    self.bounds = bounds
    self.children = []
    self.types = ["display"]
    self.name = "move_button_action"
    self.entity_state = None
    self.active = False
    self.verbose = False 
    return
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.active == False:
      return False
    if data == None:
      return False
    return True
  
  def act(self, data):
    if self.condition_to_act(data):
      
      # move the button
      self.move_button(self.entity_state)
      
      # change the button color
      self.set_button_color(self.entity_state)
      
      # wait to be moved again
      self.active = False
    return
  
  # change the rect button's location
  def move_button(self, button):
    # create random location
    location = ( random.randint( 1, self.bounds[0]-button.bounds[2] ), random.randint( 1, self.bounds[1]-button.bounds[3] ) )
    button.move( location )
    if self.verbose:
      print( f"{self.name} moving {self.entity_state.name} to {location}" )
    return
  
  # change the rect button's color
  def set_button_color(self, button):
    # create random color
    color = ( random.randint(25, 255), random.randint(25, 255), random.randint(25, 255) )
    button.set_color( color )
    if self.verbose:
      print( f"{self.name} changing {self.entity_state.name} color to {color}" )
    return