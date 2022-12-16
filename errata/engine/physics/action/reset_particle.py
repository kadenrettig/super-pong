# ADAM COPELAND, CPSC 4160, FALL 2022
# Action that resets the position of a particle

# passes the center position from the entity to the child actions
class ResetParticle():
  def __init__(self, index, spawn):
    self.types = ["position"]
    self.particle_index = index
    self.start_location = [spawn[0], spawn[1]]
    self.name = "reset_particle_action"
    self.verbose = False 
    self.children = []
    return
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False
    if self.particle_index >= len(self.entity_state.position):
      return False
    if self.entity_state.active_particle[self.particle_index] == False:
      return False
    return True 
  
  def act(self, data):
    if self.condition_to_act( data ):

      # sets the particles current position to that of the passed in "spawn" location
      self.entity_state.position[self.particle_index][0] = self.start_location[0]
      self.entity_state.position[self.particle_index][1] = self.start_location[1]
      self.entity_state.velocity[self.particle_index][0] = - self.entity_state.velocity[self.particle_index][0]
      
      for c in self.children:
        c.act( None )
        
      if self.verbose:
        print( f"{self.name} for {self.entity_state.name}" )
    return 