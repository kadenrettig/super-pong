# ADAM COPELAND, CPSC 4160, FALL 2022
# Level manager entity. Responsible for loading and closing a list of levels.

class LevelManager():
    def __init__(self, game, display, levels, name="level_manager"):
        self.levels = levels
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
  
    # Method that loads the current level
    def load_level(self):
        if (self.counter < len(self.levels)):
            print(f"LOADING level {self.counter}")
        
            for e in self.levels[self.counter]:
                self.game_loop.insert_entity(e)
                self.display.insert_entity(e)
        return
    
    # Method that closes the last loaded level's contents
    def close_level(self):
        for le in self.levels[self.counter]:
            for a in le.actions:
                self.game_loop.remove_action(a)
                self.display.remove_action(a)
                
        # Update to the next level
        if (self.counter < len(self.levels)):
            self.counter += 1
            print(f"Counter up to {self.counter}")
        else:
            print("Out of levels!")