# KADEN RETTIG, CPSC 4160, FALL 2022
# solve for euler action
# euler is the simplest and crudest of the possible solvers

class EulerSolveAction():
  def __init__(self):
    self.types = ["physics"]
    self.entity_state = None 
    self.dt = 1.0 
    self.name = "euler_solve_action"
    self.verbose = False 
    self.children = []
    
  def condition_to_act(self, data):
    if self.entity_state == None:
      return False
    if self.entity_state.active == False:
      return False 
    # if there are fewer than 2 children the solver is not useable
    if len(self.children) < 2:
      return False
    return True 
    
  def act(self, data):
    if self.condition_to_act( data ):
      # first two children are part of the solve
      self.children[0].dt = float( self.dt )
      self.children[1].dt = float( self.dt )
      self.children[0].act( data )
      self.children[1].act( data )
      
      # any other children operate here
      for c in self.children[2:]:
        c.act( data )
      if self.verbose:
        print( f"{self.name} for {self.entity_state.name}")
    return