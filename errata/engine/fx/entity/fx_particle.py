# KADEN RETTIG, CPSC 4160, FALL 2022
# entity to represent a particle

class FXParticle():
  def __init__(self, name="fx_particle"):
    self.position = []
    self.velocity = []
    self.acceleration = []
    self.id = []
    self.age = []
    self.lifetime = []
    self.color = [] 
    self.name = name
    self.actions = []
    self.active = True
    self.verbose = False
    return
  
  def insert_action(self, a):
    a.entity_state = self
    self.actions.append(a)
    return
  
  def make_particle(self):
    self.position.append( (0, 0) )
    self.velocity.append( 0 )
    self.acceleration.append( 0 )
    self.id.append( len(self.id) )
    self.age.append( 0 )
    self.lifetime.append( 0 )
    self.color.append( (0, 0, 0) )
    return
  
  