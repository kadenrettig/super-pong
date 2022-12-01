# KADEN RETTIG, CPSC 4160, FALL 2022
# a basic button

class Button():
  def __init__(self, bounds=(100, 100, 100, 100), color=(128, 128, 128), msg="", name="button"):
    self.bounds = bounds
    self.color = color
    self.message = msg
    self.border = False
    self.border_color = (255, 255, 255)
    self.border_thickness = 5
    self.template = None 
    self.actions = [] 
    self.name = name 
    self.verbose = False 
    self.active = True 
    return
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append( a )
    return
  
  # determines whether mouse pos is inside the rect
  def hover(self, pos):
    if pos[0] < self.bounds[0]:
      return False 
    if pos[0] > self.bounds[2] + self.bounds[0]:
      return False 
    if pos[1] < self.bounds[1]:
      return False 
    if pos[1] > self.bounds[3] + self.bounds[1]:
      return False 
    return True
  
  # changes the location of a letter/text object
  def move(self, location):
    if self.verbose:
      print( f"moving from ({self.bounds[0]}, {self.bounds[1]}) to ({location[0]}, {location[1]})" )
    self.bounds = ( location[0], location[1], self.bounds[2], self.bounds[3] )
    return
  
  # change the color of at letter/text object
  def set_color(self, color):
    if self.verbose:
      print( f"color of {self.name} is changing from {self.color} to {color}" )
    self.color = color 