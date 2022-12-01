# KADEN RETTIG, CPSC 4160, FALL 2022
# a hud entity

class HUD():
  def __init__(self, name="HUD"):
    self.template = None 
    self.actions = [] 
    self.children = []
    self.name = name 
    self.verbose = False 
    self.active = True 
    return
  
  def insert_action(self, a):
    a.entity_state = self 
    self.actions.append( a )
    
    if self.verbose:
      print(f"inserting {a.name} into HUD actions")
    return