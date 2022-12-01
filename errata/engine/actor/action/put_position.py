# KADEN RETTIG, CPSC 4160, FALL 2022
# puts the position passed to the action into the center location of the bounds of the entity

class PutPositionAction():
  def __init__(self):
    self.types = ["position"]
    self.entity_state = None 
    self.name = "put_position_action"
    self.verbose = False 
    self.children = []
    return

  def condition_to_act(self, data):
    if self.entity_state == None:
      return False 
    if self.entity_state.active == False:
      return False
    if len(data) != 2:
      return False
    return True 
  
  def act(self, data):
    if self.condition_to_act( data ):
      self.entity_state.location = list(data)
      #print( f"moving {self.entity_state.name} to {list(data)}")
      for c in self.children:
        c.act( data )
      if self.verbose:
        print( f"{self.name} for {self.entity_state.name}")
    return