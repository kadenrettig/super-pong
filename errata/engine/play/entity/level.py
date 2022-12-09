# ADAM COPELAND, CPSC 4160, FALL 2022
# Level Entity
import gc

class Level():
    def __init__(self, game, display, content, name="level_0"):
        self.level_content = content
        self.game_loop = game
        self.display = display
        self.actions = []
        self.counter = 0
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append( a )
        return
  
    def load_level(self):
        for e in self.level_content:
            self.game_loop.insert_entity(e)
            self.display.insert_entity(e)

    def close_level(self):
        for le in self.level_content:
            for a in le.actions:
                self.game_loop.remove_action(a)
                self.display.remove_action(a)
                
        
