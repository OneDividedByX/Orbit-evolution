from orbit_decay.procedures.graphing import *

def oscilation(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants):
    return graph_oscilation(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants)

def path(x_0,y_0,v_x0,v_y0,t_0,speed,planet_Radius,h,func_constants,epsilon,time_step_max):
    return graph_path(x_0,y_0,v_x0,v_y0,t_0,speed,planet_Radius,h,func_constants,epsilon,time_step_max)

def planet(planet_Radius):
    return graph_planet(planet_Radius)

def trajectory(x_0,y_0,v_x0,v_y0,t_0,planet_Radius,h,epsilon,time_step_max,func_constants):
    return graph_trajectory(x_0,y_0,v_x0,v_y0,t_0,planet_Radius,h,epsilon,time_step_max,func_constants)