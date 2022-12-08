##### ENTITIES #####

def make_particles():
  import errata.engine.physics.entity.particle as pt 
  return pt.Particle()

def make_gravity_force():
  import errata.engine.physics.entity.gravity_force as f 
  return f.GravityForce()

def make_spring_force():
  import errata.engine.physics.entity.spring_force as f 
  return f.SpringForce()

def make_drag_force():
  import errata.engine.physics.entity.drag_force as f 
  return f.DragForce()

def make_rectangle_collider( llc, urc ):
  import errata.engine.physics.entity.rectangle_collider as rc 
  return rc.RectangleCollider( llc, urc )

##### ACTIONS #####

def make_gravity_action():
  import errata.engine.physics.action.enforce_gravity as eg 
  return eg.GravityForceAction()

def make_spring_action():
  import errata.engine.physics.action.enforce_spring as es 
  return es.SpringForceAction()

def make_drag_action():
  import errata.engine.physics.action.enforce_drag as ed 
  return ed.DragForceAction()

def make_position_solve_action():
  import errata.engine.physics.action.position_solve as ps 
  return ps.PositionSolveAction() 

def make_velocity_solve_action():
  import errata.engine.physics.action.velocity_solve as vs 
  return vs.VelocitySolveAction() 

def make_euler_solve_action():
  import errata.engine.physics.action.euler_solve as es 
  return es.EulerSolveAction()

def make_pick_position_action( index ):
  import errata.engine.physics.action.pick_position as pp 
  return pp.PickPositionAction( index )

def make_reset_particle_action( index, spawn ):
  import errata.engine.physics.action.reset_particle as rp 
  return rp.ResetParticle( index, spawn )

def make_inside_rectangle_collision():
  import errata.engine.physics.action.inside_rectangle_collision as irc 
  return irc.InsideRectangleCollisionAction()

def make_outside_rectangle_collision():
  import errata.engine.physics.action.outside_rectangle_collision as orc
  return orc.OutsideRectangleCollisionAction()

def make_activate_action():
  import errata.engine.physics.action.activate as act 
  return act.Activate()

def make_deactivate_action():
  import errata.engine.physics.action.deactivate as act 
  return act.Deactivate()