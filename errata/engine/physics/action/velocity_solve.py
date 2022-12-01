# KADEN RETTIG, CPSC 4160, FALL 2022
# solve for velocity action

class VelocitySolveAction():
  def __init__(self):
    self.types = ["physics"]
    self.entity_state = None 
    self.dt = 1.0
    self.name = "velocity_solve_action"
    self.verbose = False 
    self.children = []
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False
    return True 
  
  def act(self, data):
    if self.condition_to_act( data ):
      for i in range( 0, len(self.entity_state.acceleration) ):
        if self.entity_state.active_particle[i]:
          self.entity_state.acceleration[i][0] = 0.0
          self.entity_state.acceleration[i][1] = 0.0
      
      # the assumption is that the children will compute the acceleration from force(s)
      # for this, the children need the entity_state (particles)
      # and the children must be called *prior* to updating the velocity
      for c in self.children:
        c.act( self.entity_state )
      
      # now we can update velocity
      for i in range( 0, len(self.entity_state.velocity) ):
        if self.entity_state.active_particle[i]:
          self.entity_state.velocity[i][0] = self.entity_state.velocity[i][0] + self.dt * self.entity_state.acceleration[i][0]
          self.entity_state.velocity[i][1] = self.entity_state.velocity[i][1] + self.dt * self.entity_state.acceleration[i][1]
      if self.verbose:
        print( f"{self.name} for {self.entity_state.name}" )
    return 