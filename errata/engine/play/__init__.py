##### ENTITIES #####

def make_frame_viewer( ssize ):
  import errata.engine.play.entity.frame_viewer as fv
  frameViewer = fv.FrameViewer( ssize )
  return frameViewer

def make_game_looper( content = None ):
  import errata.engine.play.entity.game_looper as gl
  looper = gl.GameLooper()
  if content != None:
    for c in content:
      looper.insert_entity(c)
  return looper

def make_level(gameloop, display, content, name):
  import errata.engine.play.entity.level as lvl
  return lvl.Level(gameloop, display, content, name)

def make_level_manager(gameloop, display, levels, name):
  import errata.engine.play.entity.level_manager as lm
  return lm.LevelManager(gameloop, display, levels, name)

##### ACTIONS #####

# action to close the viewer
def make_close_viewer_action():
  import errata.engine.play.action.close_viewer as cv
  return cv.CloseViewer()

# action to refresh the screen 
def make_display_screen_action():
  import errata.engine.play.action.display_screen as ds
  return ds.DisplayScreen()

# action to resize the viewer
def make_screen_resize_action():
  import errata.engine.play.action.screen_resize as sr 
  return sr.ScreenResize()

def make_load_level_action():
  import errata.engine.play.action.load_level as load
  return load.LoadLevel()

def make_close_level_action():
  import errata.engine.play.action.close_level as close
  return close.CloseLevel()