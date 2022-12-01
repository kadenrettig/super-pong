# KADEN RETTIG, CPSC 4160, FALL 2022
# action to detect whether a physics-influenced 
# entity is within a rectangle collider

class InsideRectangleCollisionAction():
  def __init__(self):
    self.types = ["physics"]
    self.entity_state = None 
    self.name = "inside_rectangle_action"
    self.verbose = False 
    self.children = []
    return 
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False 
    if data == None:
      return False 
    return True 
  
  # data is the particles
  def act(self, data):
    if self.condition_to_act( data ):
      for i in range( 0, len(data.position) ):
        if data.active_particle[i]:
          # 1st lower left corner
          if data.position[i][0] < self.entity_state.llc[0]:
            data.position[i][0] = 2.0 * self.entity_state.llc[0] - data.position[i][0]
            data.velocity[i][0] = -data.velocity[i][0] 
          # 1st upper right corner
          elif data.position[i][0] > self.entity_state.urc[0]:
            data.position[i][0] = 2.0 * self.entity_state.urc[0] - data.position[i][0]
            data.velocity[i][0] = -data.velocity[i][0]
          # 2nd lower left corner
          elif data.position[i][1] < self.entity_state.llc[1]:
            data.position[i][1] = 2.0 * self.entity_state.llc[1] - data.position[i][1]
            data.velocity[i][1] = -data.velocity[i][1]
          # 2nd upper right corner
          elif data.position[i][1] > self.entity_state.urc[1]:
            data.position[i][1] = 2.0 * self.entity_state.urc[1] - data.position[i][1]
            data.velocity[i][1] = -data.velocity[i][1]
      
      for c in self.children:
        c.act( data )
      if self.verbose:
        print( f"{self.name} for {self.entity_state.name}" )
    return