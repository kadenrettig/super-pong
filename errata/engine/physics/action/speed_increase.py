# STEPHEN SAMS, ADAM COPELAND, CPSC 4160, FALL 2022
# Action is designed to increase the velocity of the particle

class SpeedIncrease():
  def __init__(self, index, speed):
    self.types = [""]
    self.particle_index = index
    self.speed_increase = speed
    self.name = "speed_increase_action"
    self.verbose = False 
    self.children = []
    return
  
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False
    return True
  
  def act(self, data):
    
    # Add horizontal speed (add if positive, subtract if negative)
    if self.entity_state.velocity[self.particle_index][0] >= 0:
      self.entity_state.velocity[self.particle_index][0] += self.speed_increase[0]
    else:
      self.entity_state.velocity[self.particle_index][0] -= self.speed_increase[0]
      
    # Add vertical speed (add if positive, subtract if negative)
    if self.entity_state.velocity[self.particle_index][1]:
      self.entity_state.velocity[self.particle_index][1] += self.speed_increase[1]
    else:
      self.entity_state.velocity[self.particle_index][1] -= self.speed_increase[1]

    for c in self.children:
      c.act( None )
        
    if self.verbose:
      print( f"{self.name} for {self.entity_state.name}" )
    return 