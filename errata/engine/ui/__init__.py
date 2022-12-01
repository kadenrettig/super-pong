##### ENTITIES #####

def make_button( info ):
  import errata.engine.ui.entity.button as b
  # bounds, color, message, name
  if len(info) == 4:
    button = b.Button( info[0], info[1], info[2], info[3] )
  # bounds, color, message
  if len(info) == 3:
    button = b.Button( info[0], info[1], info[2] )
  # bounds, color
  else:
    button = b.Button( info[0], info[1])
  return button

def make_hud():
  import errata.engine.ui.entity.hud as hud
  return hud.HUD()

##### ACTIONS #####

def make_draw_rect_button_action():
  import errata.engine.ui.action.draw_rect_button as db
  return db.DrawRectButtonAction()

def make_button_press_action():
  import errata.engine.ui.action.button_press as bp
  return bp.ButtonPress()

def make_draw_hud_action():
  import errata.engine.ui.action.draw_hud as dh 
  return dh.DrawHUD()