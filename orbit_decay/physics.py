def OrbitDecay_ODE_Function(r: list[float], t: float,
                            G: float,
                            mass_central_body: float,
                            mass_satellite: float,
                            surface_area_satellite: float,
                            env_drag_coefficient: float,
                            env_fluid_density: float):
    """Function representing the system of ordinary differential equations for orbit decay due to gravitational and drag forces.
    Args:
        r (list[float]): The current values of the dependent variables [x, y, u, v], where x and y are the position coordinates and u and v are the velocity components.
        t (float): The current value of the independent variable (time).
        G (float): The gravitational constant.
        mass_central_body (float): The mass of the central body in kilograms.
        mass_satellite (float): The mass of the satellite in kilograms.
        surface_area_satellite (float): The surface area of the satellite in square meters.
        env_drag_coefficient (float): The drag coefficient of the satellite.
        env_fluid_density (float): The density of the fluid through which the satellite is moving.
    """
    alpha = mass_central_body * G
    beta = (env_drag_coefficient * surface_area_satellite * env_fluid_density) / mass_satellite  #10^-14
    x, y, u, v = r[0], r[1],r[2],r[3]
    fxd = u
    fyd = v
    fud= (-alpha*(x/(((x**2)+(y**2))**1.5)))-(u*beta*(((u**2)+(v**2))**0.5))
    fvd= (-alpha*(y/(((x**2)+(y**2))**1.5)))-(v*beta*(((u**2)+(v**2))**0.5))
    return [fxd, fyd, fud, fvd]