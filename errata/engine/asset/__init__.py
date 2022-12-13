##### ENTITIES #####
def make_image( location, size, image_name, name ):
  import errata.engine.asset.entity.image as img 
  return img.Image( location, size, image_name, name )


##### ACTIONS #####
def make_draw_image_action():
  import errata.engine.asset.action.draw_image as img 
  return img.DrawImageAction()