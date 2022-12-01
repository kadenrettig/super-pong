##### ENTITIES #####

def make_track( path, track ):
  import errata.engine.sound.entity.track as tk
  return tk.Track( path, track )

##### ACTIONS #####

def make_bgm_action( duration ):
  import errata.engine.sound.action.bgm as bgm
  return bgm.BGM( duration )

def make_sound_action( track_name ):
  import errata.engine.sound.action.sound as sfx
  return sfx.Sound( track_name )