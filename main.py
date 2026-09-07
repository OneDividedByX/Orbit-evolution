import orbit_decay.graphics as graphics

epsilon=100.0; time_step_max=1000000

R_p=6378000.0; R_core_inner=1200000; R_core_outer=2750000; R_suffer_mantle=5400000; R_rigid_mantle=6300000.0


# Constantes naturales
M=5.972*10**24
G=6.673*10**(-11)

# Constantes condicionadas
C=2.2
A=0.72
rho=7*10**-7
# m=7.349*10**22 # moon
m=419725 # ISS

func_constants=(M,m,G,C,A,rho)

h=10
# tpoints = np.arange(0, 9500, h)  #(t_0,t_f,h)
t_0=0.0

# x_0,y_0,v_x0,v_y0=384400000,0, 0,1000  # moon
x_0,y_0,v_x0,v_y0=R_p+400000, 0, 0,10000  # ISS
r_0 = [x_0,y_0,v_x0,v_y0] #(x_0, y_0, v_{x_0}, v_{y_0})
v=(v_x0**2+v_y0**2)**0.5

planet_Radius = (R_core_inner,R_core_outer,R_suffer_mantle,R_rigid_mantle,R_p)
# graph.trajectory(x_0,y_0,v_x0,v_y0,t_0,planet_Radius,h,epsilon,time_step_max,func_constants)


graphics.path(x_0,y_0,v_x0,v_y0,t_0,100,planet_Radius,h,func_constants,epsilon,time_step_max)