from orbit_decay.graphics import GraphUniverse
from orbit_decay.objects import Universe, UniverseBody, UniverseInteraction
import matplotlib.pyplot as plt

R_p=6378000.0

x_0,y_0,v_x0,v_y0=R_p+400000, 0, 0,10000  # ISS
r_0 = [x_0,y_0,v_x0,v_y0]


universe = Universe("My Universe")

a = UniverseBody(universe, name="Earth", mass=5.972*10**24, radius=6378000.0, position=[0.0, 0.0], velocity=[0.0, 0.0], color="blue")
b = UniverseBody(universe, name="ISS", mass=419725, radius=0, position=[6378000.0 + 400000.0, 0.0], velocity=[50, 10000.0], color="red")

g = GraphUniverse(universe)
fig, ax = plt.subplots()
# g.plot_initial(fig, ax)

interaction = UniverseInteraction(a, b)
# interaction.trajectory_Loop(-1)
R_0=(float(r_0[0])**2+float(r_0[1])**2)**0.5
plt.xlim(-2*R_0, 2*R_0)
plt.ylim(-2*R_0, 2*R_0)
g.plot_loop(a,b,fig,ax,5)
plt.grid()
plt.gca().set_aspect('equal')
plt.show()
