# KADEN RETTIG, CPSC 4160, FALL 2022

# passes the center position from the entity to the child actions
class PickPositionAction():
  def __init__(self, index):
    self.types = ["position"]
    self.particle_index = index
    self.entity_state = None 
    self.name = "pick_position_action"
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
      new_data = list( self.entity_state.position[self.particle_index] )
      
      for c in self.children:
        c.act( new_data )
        
      if self.verbose:
        print( f"{self.name} for {self.entity_state.name}" )
    return 