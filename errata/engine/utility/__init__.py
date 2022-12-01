##### ENTITIES #####

def make_timer():
  import errata.engine.utility.entity.timer as tm 
  return tm.Timer()

def make_total_counter():
  import errata.engine.utility.entity.total_counter as tc 
  return tc.TotalCounter()

def make_success_counter():
  import errata.engine.utility.entity.success_counter as sc
  return sc.SuccessCounter()

##### ACTIONS #####

def make_activate_action():
  import errata.engine.utility.action.activate as av
  return av.Activate()

def make_deactivate_action():
  import errata.engine.utility.action.deactivate as dv
  return dv.Deactivate()

def make_increment_action( value ):
  import errata.engine.utility.action.increment as ic
  return ic.Increment( value )

def make_update_action():
  import errata.engine.utility.action.update as up
  return up.Update()

def make_start_action():
  import errata.engine.utility.action.start as st 
  return st.Start()

def make_alarm_action( wait, audible ):
  import errata.engine.utility.action.alarm as al 
  return al.Alarm( wait, audible )