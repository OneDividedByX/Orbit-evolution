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


from orbit_decay.objects import UniverseBody, Universe, UniverseInteraction
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.axes import Axes
class GraphUniverse:
    def __init__(self, universe: Universe):
        self.universe = universe
        
    def plot_initial(self, fig: Figure, ax: Axes):
        """Initialize the plot with the initial positions of the bodies in the universe."""
        for body in self.universe.bodies.values():
            if body.radius > 0:                
                circle = plt.Circle((body.current_position[0], body.current_position[1]), body.radius, color=body.color, alpha=0.5)
                ax.add_patch(circle)
            else:
                plt.plot(body.current_position[0], body.current_position[1], 'o', color=body.color)  # Plot point for bodies with zero radius
        
    
    def _update_positions(self, body: UniverseBody, x_data: float, y_data: float, line: plt.Line2D):
        body.update_position([x_data, y_data])
        # y_data.append(body.current_position[1])
        line.set_data(zip(*body.list_position))
        # print(x_data, y_data, line, "dfdff")
        
    def plot_loop(self, body1: UniverseBody, body2: UniverseBody , fig: Figure, ax: Axes, delta_time = 1.0):

        line = ax.plot(body2.list_position,color = 'steelblue',linestyle='-')[0]
        
        def update(data):
            x_data, y_data = data
            self._update_positions(body2, x_data, y_data, line)
            return line,
        def initial():
            self.plot_initial(fig, ax)
            return line,
        interaction = UniverseInteraction(body1, body2)
        ani = animation.FuncAnimation(
            fig, 
            update,
            frames = lambda: interaction.trajectory_Loop(delta_time), # Nuestra función indefinida
            init_func = initial, 
            blit=True, 
            interval=10, # Tiempo en milisegundos entre actualizaciones
            save_count=100 # Evita advertencias de memoria reteniendo los últimos 100 frames
        )
        return ani

a = UniverseBody(name="Earth", mass=5.972*10**24, radius=6378000.0, position=[0.0, 0.0], velocity=[0.0, 0.0], color="blue")
b = UniverseBody(name="ISS", mass=419725, radius=0, position=[6378000.0 + 400000.0, 0.0], velocity=[0.0, 10000.0], color="red")

g = GraphUniverse(Universe())
fig, ax = plt.subplots()
# g.plot_initial(fig, ax)

interaction = UniverseInteraction(a, b)
# interaction.trajectory_Loop(-1)
R_0=(float(r_0[0])**2+float(r_0[1])**2)**0.5
plt.xlim(-2*R_0, 2*R_0)
plt.ylim(-2*R_0, 2*R_0)
ani = g.plot_loop(a,b,fig,ax,100)
plt.grid()
plt.gca().set_aspect('equal')
plt.show()

# graphics.path(x_0,y_0,v_x0,v_y0,t_0,100,planet_Radius,h,func_constants,epsilon,time_step_max)