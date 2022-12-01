# KADEN RETTIG, CPSC 4160, FALL 2022
# specific to this game: move the button to a random position

class GenerateMessage():
  def __init__(self):
    self.total = 0
    self.successes = 0
    self.types = ["display"]
    self.entity_state = None
    self.name = "generate_message_action"
    self.children = []
    self.active = False
    self.verbose = False 
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
    if self.condition_to_act(data):
      
      # get new counter values 
      self.update_total()
      self.update_successes()
      
      # update the counter displays
      self.update_counters()
      
      # wait to be moved again
      self.active = False
    return
  
  def update_counters(self):
    for c in self.entity_state.children:
      if c.name == "hud_total":
        c.text = f"total: {self.total}"
      if c.name == "hud_success":
        c.text = f"successes: {self.successes}"
    return
  
  # update the total counter
  def update_total(self):
    for c in self.children:
      if c.name == "total_counter":
        self.total = c.counter
    return
  
  # update the success counter
  def update_successes(self):
    for c in self.children:
      if c.name == "success_counter":
          self.successes = c.counter
    return