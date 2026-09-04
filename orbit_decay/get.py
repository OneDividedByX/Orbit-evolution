from orbit_decay.procedures.getting import *

def last_path_step(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants):
    return get_last_path_step(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants)

def trajectory(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants):
    return get_trajectory(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants)

def planet_layers(planet_Radius):
    return planet_layers(planet_Radius)