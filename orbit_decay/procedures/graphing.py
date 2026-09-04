from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from orbit_decay.iterative_method import rk4
from orbit_decay.procedures.getting import get_trajectory, get_planet_layers

def graph_oscilation(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants):
    xpoints, ypoints ,upoints, vpoints,Tpoints=get_trajectory(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants)
    plt.grid()
    plt.plot(Tpoints, xpoints)
    plt.plot(Tpoints, ypoints)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("x(t) (m) vs y(t) (m)")
    plt.title("Decaimiento en los ejes")
    plt.savefig('plotted_images/decaimiento.png')
    plt.show()
#########################################################
######################################################### 
def update_path(frame,x,y,Tpoints,Tpoints_copy,r,h,func_constants,graph,R_p,epsilon,time_step_max,time_counter,speed):
    R=(float(r[0])**2+float(r[1])**2)**0.5; t=Tpoints[-1]
    if (abs(R-R_p)>=epsilon and t<time_step_max):        
        r += rk4(r, t, h,func_constants)
        Tpoints_copy.append(t) # One step in time before
        t=t+h
        Tpoints.append(t) # Current time step
        # updating the data
        x.append(r[0]); y.append(r[1])
        if np.abs(time_counter+speed-Tpoints[-1])>=np.abs(time_counter+speed-Tpoints_copy[-1]): # if Current time step increase the distance to next time_counter then One step in time before reached minimum distance
            time_counter=time_counter+speed
            graph.set_xdata(x)
            graph.set_ydata(y)

# h: power of 10
# Recommended h<speed
#########################################################
#########################################################
def graph_path(x_0,y_0,v_x0,v_y0,t_0,speed,planet_Radius,h,func_constants,epsilon,time_step_max):
    R_p=planet_Radius[4]
    if speed>0:
        rate=1/speed*1000
    else: rate=200
    ###################################
    x=[x_0];  y=[y_0]; Tpoints=[t_0]; Tpoints_copy=[]; r= np.array([x_0,y_0,v_x0,v_y0], float); time_counter=0
    fig, ax = plt.subplots()
    graph = ax.plot(x,y,color = 'steelblue')[0]
    R_0=(float(r[0])**2+float(r[1])**2)**0.5
    # plt.xlim(-18*10**6, 18*10**6)
    # plt.ylim(-12*10**6, 12*10**6)
    # plt.xlim(-2.7*R_p, 2.7*R_p)
    # plt.ylim(-1.8*R_p, 1.8*R_p)
    plt.xlim(-2*R_0, 2*R_0)
    plt.ylim(-2*R_0, 2*R_0)
    plt.xlabel("x(t) (m)")
    plt.ylabel("y(t) (m)")
    plt.plot(x_0, y_0,'o',color='steelblue') # Also available with scatter plots
    c0,c1,c2,c3,c4=get_planet_layers(planet_Radius)
    ax.add_patch(c0); ax.add_patch(c1); ax.add_patch(c2); ax.add_patch(c3); ax.add_patch(c4) 
    anim = FuncAnimation(fig, update_path, fargs=(x,y,Tpoints,Tpoints_copy,r,h,func_constants,graph,R_p,epsilon,time_step_max,time_counter,speed), frames=None,interval=rate,cache_frame_data=False)
    plt.grid()
    plt.gca().set_aspect('equal')
    plt.show()
    # anim.save(filename="plotted_images/plot_path.gif", writer="pillow")
    # anim.save(filename="plotted_images/plot_path.apng", writer="pillow")
#########################################################
#########################################################
def graph_planet(planet_Radius):
    R_core_inner,R_core_outer,R_suffer_mantle,R_rigid_mantle,R_p=planet_Radius[0], planet_Radius[1], planet_Radius[2], planet_Radius[3], planet_Radius[4]
    c0,c1,c2,c3,c4=get_planet_layers(R_core_inner,R_core_outer,R_suffer_mantle,R_rigid_mantle,R_p)
    fig, ax = plt.subplots()
    ax.add_patch(c0); ax.add_patch(c1); ax.add_patch(c2); ax.add_patch(c3); ax.add_patch(c4)    
#########################################################
#########################################################
def graph_trajectory(x_0,y_0,v_x0,v_y0,t_0,planet_Radius,h,epsilon,time_step_max,func_constants):
    R_p=planet_Radius[4]
    c0,c1,c2,c3,c4=get_planet_layers(planet_Radius)
    fig, ax = plt.subplots()
    ax.add_patch(c0); ax.add_patch(c1); ax.add_patch(c2); ax.add_patch(c3); ax.add_patch(c4)
    plt.grid()
    # plt.xlim(-18*10**6, 18*10**6)
    # plt.ylim(-12*10**6, 12*10**6)
    # plt.xlim(-2.7*R_p, 2.7*R_p)
    # plt.ylim(-1.8*R_p, 1.8*R_p)
    r_0 = np.array([x_0,y_0,v_x0,v_y0], float) #(x_0, y_0, v_{x_0}, v_{y_0})
    R_0=(float(r_0[0])**2+float(r_0[1])**2)**0.5
    plt.xlim(-2*R_0, 2*R_0); plt.ylim(-2*R_0, 2*R_0); plt.xlabel("x(t) (m)"); plt.ylabel("y(t) (m)")    
    xpoints, ypoints ,upoints, vpoints,Tpoints=get_trajectory(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants)
    plt.plot(xpoints, ypoints,color='steelblue')
    plt.plot(x_0, y_0,'o',color='steelblue') # Also available with scatter plots
    plt.title("Degeneración de la órbita del satélite",fontsize=15)
    plt.gca().set_aspect('equal')
    plt.show()
    fig.savefig('plotted_images/plotcircles.png') #Generamos la grafica de la trayectoria
    print(f'El impacto se produce aproximadamente en ({xpoints[-1]},{ypoints[-1]}) m despues de {Tpoints[-1]} s')