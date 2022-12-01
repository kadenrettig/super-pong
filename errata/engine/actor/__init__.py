##### ENTITIES #####

def make_rectangle( info ):
  import errata.engine.actor.entity.rectangle as rect
  # dimensions, color
  if len(info) == 2:
    rectangle = rect.Rectangle( info[0], info[1] )
  else:
    rectangle = rect.Rectangle( info[0], info[1], info[2] )
  return rectangle

def make_circle( info ):
  import errata.engine.actor.entity.circle as circ
  # radius, location, color
  if len(info) == 3:
    circle = circ.Circle( info[0], info[1], info[2] )
  else:
    circle = circ.Circle( info[0], info[1], info[2], info[3] )
  return circle

def make_text( info ):
  import errata.engine.actor.entity.text as char
  # font size, location, color, character
  if len(info) == 4:
    text = char.Text( info[0], info[1], info[2], info[3] )
  else:
    text = char.Text( info[0], info[1], info[2], info[3], info[4] )
  return text

##### ACTIONS #####

def make_draw_rectangle_action():
  import errata.engine.actor.action.draw_rectangle as dr
  return dr.DrawRectAction()

def make_draw_circle_action():
  import errata.engine.actor.action.draw_circle as dc
  return dc.DrawCircleAction()

def make_draw_text_action():
  import errata.engine.actor.action.draw_text as dl
  return dl.DrawTextAction()

def make_guess_letter_action( word ):
  import errata.engine.actor.action.guess_letter as dl
  return dl.GuessLetterAction( word )

def make_put_position_action():
  import errata.engine.actor.action.put_position as pp 
  return pp.PutPositionAction()

def make_is_inside_action():
  import errata.engine.actor.action.is_inside as i 
  return i.IsInside()