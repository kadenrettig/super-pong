# KADEN RETTIG, CPSC 4160, FALL 2022
# drag force action

class DragForceAction():
  def __init__(self):
    self.types = ["force"]
    self.entity_state = None 
    self.name = "drag_force_action"
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
  
  def act(self, data):
    # the data is the particle entity state 
    if self.condition_to_act( data ):
      # change the active status of particles before applying physics
      # the first child is always is_inside
      for c in self.children[:1]:
        c.act( data )
      
      # apply physics
      for i in range( 0, len(data.acceleration) ):
        if data.active_particle[i]:
          data.acceleration[i][0] = data.acceleration[i][0] - data.velocity[i][0] * self.entity_state.drag_constant
          data.acceleration[i][1] = data.acceleration[i][1] - data.velocity[i][1] * self.entity_state.drag_constant
          
      # reactivate particles
      for c in self.children[1:]:
        c.act( None )
          
    if self.verbose:
      print( f"{self.name} for {self.entity_state.name}")
    return