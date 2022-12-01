##### MOVER #####

def make_mover( bounds ):
  import move as mv
  return mv.Move( bounds )

def make_generate_message():
  import generate_message as gm 
  return gm.GenerateMessage()