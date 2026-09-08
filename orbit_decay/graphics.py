from orbit_decay.objects import UniverseBody
from orbit_decay.procedures.graphing import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def oscilation(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants):
    return graph_oscilation(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants)

def path(x_0,y_0,v_x0,v_y0,t_0,speed,planet_Radius,h,func_constants,epsilon,time_step_max):
    return graph_path(x_0,y_0,v_x0,v_y0,t_0,speed,planet_Radius,h,func_constants,epsilon,time_step_max)

def planet(planet_Radius):
    return graph_planet(planet_Radius)

def trajectory(x_0,y_0,v_x0,v_y0,t_0,planet_Radius,h,epsilon,time_step_max,func_constants):
    return graph_trajectory(x_0,y_0,v_x0,v_y0,t_0,planet_Radius,h,epsilon,time_step_max,func_constants)


from orbit_decay.objects import UniverseBody, Universe
# class GraphUniverseObjects:
#     def __init__(self, *args: UniverseBody):
#         self.universe = list(args)

# a = UniverseBody(name="Earth", mass=5.972*10**24, radius=6378000.0, position=[0.0, 0.0], velocity=[0.0, 0.0])
# b = UniverseBody(name="ISS", mass=419725, radius=10.0, position=[6378000.0 + 400000.0, 0.0], velocity=[0.0, 10000.0])

# g = GraphUniverseObjects(a, b)
# print(g.universe[0].name, g.universe[1].name)

