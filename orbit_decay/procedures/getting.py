import matplotlib.pyplot as plt
from iterative_method import rk4
from linear_algebra import sum_vectors

def get_last_path_step(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants):
    xpoints, ypoints ,upoints, vpoints,Tpoints=get_trajectory(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants)
    x_f=xpoints[-1]; y_f=ypoints[-1]; v_xf=upoints[-1]; v_yf=vpoints[-1]; t_f=Tpoints[-1]
    return x_f, y_f, v_xf, v_yf, t_f

def get_trajectory(r_0,t_0,R_p,h,epsilon,time_step_max,func_constants):
    r=r_0.copy(); R=(float(r[0])**2+float(r[1])**2)**0.5; t=t_0; Tpoints = [t_0]; xpoints, ypoints ,upoints, vpoints  = [r[0]], [r[1]],[r[2]],[r[3]]
    while(abs(R-R_p)>=epsilon and Tpoints[-1]<time_step_max):        
        R=(float(r[0])**2+float(r[1])**2)**0.5
        r = sum_vectors(r,rk4(r, t, h,func_constants))
        xpoints.append(r[0])
        ypoints.append(r[1])
        upoints.append(r[2])
        vpoints.append(r[3])
        t=t+h
        Tpoints.append(t)
    return xpoints, ypoints ,upoints, vpoints,Tpoints

def get_planet_layers(planet_Radius):
    R_core_inner,R_core_outer,R_suffer_mantle,R_rigid_mantle,R_p=planet_Radius[0], planet_Radius[1], planet_Radius[2], planet_Radius[3], planet_Radius[4]
    circle0 = plt.Circle((0, 0),R_p,color='aqua')
    circle1 = plt.Circle((0, 0),R_rigid_mantle,color='brown')
    circle2 = plt.Circle((0, 0),R_suffer_mantle,color='orange')
    circle3 = plt.Circle((0, 0),R_core_outer,color='gold') #Representacion del planeta como un circulo en el plano
    circle4 = plt.Circle((0, 0),R_core_inner,color='yellow')
    return circle0,circle1,circle2,circle3,circle4