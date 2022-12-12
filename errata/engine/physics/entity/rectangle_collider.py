# KADEN RETTIG, CPSC 4160, FALL 2022
# rectangular collider entity for collision simulation

class RectangleCollider():
  def __init__(self, llc = [0.0, 0.0], urc = [100.0, 100.0], name="rectangle_collider"):
    self.llc = llc 
    self.urc = urc 
    self.actions = []
    self.name = name 
    self.verbose = False 
    self.active = True 
    return 
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append( a )
    return
  
  # changes the location of a rect collider object using a given speed and direction
  # utilized by the move_player action
  def move(self, direction, speed, max_width, max_height):
    
    # calculate the new location
    dimensions = ( self.urc[0] - self.llc[0], self.urc[1] - self.llc[1])
    location = [[  self.llc[0] + speed * direction[0], 
                   self.llc[1] + speed * direction[1] ], [self.urc[0] + speed * direction[0], 
                   self.urc[1] + speed * direction[1] ] ]
    
    # ensure that the collider cannot move outside of the boundaries
    if location[1][0] > max_width: 
      location[1][0] = max_width
      location[0][0] = max_width - dimensions[0]
    elif location[0][0] < 0:
      location[0][0] = 0
      location[1][0] = 0 + dimensions[0]
    if location[1][1] > max_height:
      location[1][1] = max_height 
      location[0][1] = max_height - dimensions[1]
    elif location[0][1] < 0:
      location[0][1] = 0
      location[1][1] = 0 + dimensions[1]
      

    # assign the new location to the rect collider's variables
    self.llc = [location[0][0], location[0][1]]
    self.urc = [location[1][0], location[1][1]]
    return