# kg
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
MASS_SATELLITE=419725 # ISS

def OrbitDecay_ODE_Function(r: list[float], t: float):
    """Function representing the system of ordinary differential equations for orbit decay due to gravitational and drag forces.
    Args:
        r (list[float]): The current values of the dependent variables [x, y, u, v], where x and y are the position coordinates and u and v are the velocity components.
        t (float): The current value of the independent variable (time)."""
    alpha = MASS_CENTRAL_BODY*GRAVITATIONAL_CONSTANT
    beta = (DRAG_COEFFICIENT*SURFACE_AREA_SATELLITE*FLUID_DENSITY)/MASS_SATELLITE  #10^-14
    x, y, u, v = r[0], r[1],r[2],r[3]
    fxd = u
    fyd = v
    fud= (-alpha*(x/(((x**2)+(y**2))**1.5)))-(u*beta*(((u**2)+(v**2))**0.5))
    fvd= (-alpha*(y/(((x**2)+(y**2))**1.5)))-(v*beta*(((u**2)+(v**2))**0.5))
    return [fxd, fyd, fud, fvd]