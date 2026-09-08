from orbit_decay.graphics import GraphUniverse
from orbit_decay.objects import Universe, UniverseBody, UniverseInteraction
import matplotlib.pyplot as plt

MASS_CENTRAL_BODY=5.972*10**24

# units
GRAVITATIONAL_CONSTANT=6.673*10**(-11)

# Conditionated constants for the orbit decay simulation
# NO_UNITS
DRAG_COEFFICIENT=2.2

# m^2
SURFACE_AREA_SATELLITE=0.72

# kg/m^3
FLUID_DENSITY=7*10**-7

# kg
MASS_SATELLITE=419725
R_P=6378000.0

universe = Universe("My Universe", gravity_constant=GRAVITATIONAL_CONSTANT)

a = UniverseBody(universe,
                 name="Earth",
                 mass=MASS_CENTRAL_BODY,
                 radius=R_P,
                 position=[0.0, 0.0],
                 velocity=[0.0, 0.0],
                 color="blue",
                 atmospheric_drag_coefficient=1.0,
                 atmospheric_density=FLUID_DENSITY,
                 surface_area=1.0)
b = UniverseBody(universe,
                 name="ISS",
                 mass=MASS_SATELLITE,
                 radius=0,
                 position=[R_P + 400000.0, 0.0],
                 velocity=[5000, 5000.0],
                 color="red",
                 atmospheric_drag_coefficient=DRAG_COEFFICIENT,
                 atmospheric_density=1.0,
                 surface_area=SURFACE_AREA_SATELLITE)

g = GraphUniverse(universe)
fig, ax = plt.subplots()
interaction = UniverseInteraction(a, b)
g.plot_loop(a,b,fig,ax,10)
plt.grid()
plt.gca().set_aspect('equal')
plt.show()
