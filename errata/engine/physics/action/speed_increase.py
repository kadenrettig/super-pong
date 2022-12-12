#Action is designed to increase the velocity of the particle

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
     self.entity_state.velocity[self.particle_index][0] += self.speed_increase[0]
     self.entity_state.velocity[self.particle_index][1] += self.speed_increase[1]

     for c in self.children:
        c.act( None )
        
     if self.verbose:
        print( f"{self.name} for {self.entity_state.name}" )
     return 