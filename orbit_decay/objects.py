from orbit_decay.physics import OrbitDecay_ODE_Function
from iterative_method import ODE_METHOD
from linear_algebra import distance, sum_vectors
from typing import Callable

GRAVITATIONAL_CONSTANT=6.673*10**(-11)

class Universe:
    bodies: dict[str, UniverseBody] = {}
    
    def __init__(self, name: str, gravity_constant = GRAVITATIONAL_CONSTANT):
        """Create a new Universe object.
        Args:
            name (str): The name of the universe.
            gravity_constant (float): The gravitational constant. Determines the strength of the gravitational force between bodies.
        """
        self.name = name
        self.gravity_constant = gravity_constant
        
    @classmethod
    def register(cls, body: UniverseBody):
        """Register a new body in the universe.
        Args:
            body (UniverseBody): The body to register.
        """
        cls.bodies[body.name] = body

    def OrbitDecay_ODE_Function(self, mass_central_body: float, mass_satellite: float, surface_area_satellite: float, env_drag_coefficient: float, env_fluid_density: float):
        """Function representing the system of ordinary differential equations for orbit decay due to gravitational and drag forces.
        Args:
            mass_central_body (float): The mass of the central body in kilograms.
            mass_satellite (float): The mass of the satellite in kilograms.
            surface_area_satellite (float): The surface area of the satellite in square meters.
            env_drag_coefficient (float): The drag coefficient of the satellite.
            env_fluid_density (float): The density of the fluid through which the satellite is moving.
        """
        f : Callable[[list[float], float], list[float]] = lambda  r, t: OrbitDecay_ODE_Function(r, t, self.gravity_constant, mass_central_body, mass_satellite, surface_area_satellite, env_drag_coefficient, env_fluid_density)
        return f
    
class UniverseBody:    
    def __init__(self, universe: Universe, name: str, mass: float, radius: float, position: list[float], velocity: list[float], color: str = "b", surface_area = 1.0, atmospheric_drag_coefficient = 1.0, atmospheric_density=1.0):
        """Create a new UniverseBody object.
        Args:
            universe (Universe): The universe to which the body belongs.
            name (str): The name of the body.
            mass (float): The mass of the body in kilograms.
            radius (float): The radius of the body (m).
            position (list[float]): The initial position of the body (m).
            velocity (list[float]): The initial velocity of the body (m/s).
            color (str): The color of the body for plotting purposes.
            surface_area (float): The surface area of the body (m^2).
            atmospheric_drag_coefficient (float): The drag coefficient of the body.
            atmospheric_density (float): The density of the atmosphere through which the body is moving (kg/m^3).            
        """
        
        self.universe = universe
        self.name = name
        self.mass = mass
        self.radius = radius
        self.initial_position = position
        self.initial_velocity = velocity
        self.surface_area = surface_area
        self.atmospheric_drag_coefficient = atmospheric_drag_coefficient
        self.atmospheric_density = atmospheric_density
        self.color = color

        self.list_position = [self.initial_position]
        self.list_velocity = [self.initial_velocity]
        self.list_time = [0.0]
        
        universe.register(self)

    def update_position(self, new_position: list[float]):
        """Update the position of the body.
        Args:
            new_position (list[float]): The new position of the body.
        """
        self.list_position.append(new_position)

    def update_velocity(self, new_velocity: list[float]):
        """Update the velocity of the body.
        Args:
            new_velocity (list[float]): The new velocity of the body.
        """
        self.list_velocity.append(new_velocity)
    
    @property
    def current_position(self):
        """Current position of the body."""
        return self.list_position[-1]
    
    @property
    def current_velocity(self):
        """Current velocity of the body."""
        return self.list_velocity[-1]
    
    @property
    def current_time(self):
        """Current time of the body."""
        return self.list_time[-1]
    
class UniverseInteraction:
    def __init__(self, body1: UniverseBody, body2: UniverseBody):
        """Create a new UniverseInteraction object.
        Args:
            body1 (UniverseBody): The central body in the interaction.
            body2 (UniverseBody): The objective body in the interaction which the central body interacts with.
        """
        self.body1 = body1
        self.body2 = body2

    def trajectory_BySteps(self, delta_time: float, n_time_steps: float, tolerance_distance: float , numerical_method = "RK4"):
        """Calculate the trajectory (list of tuples) of _body2_ around _body1_ using a numerical method to solve the system of differential equations associated with the trajectory.
        Args:
            delta_time (float): The time difference between each step in the simulation. The smaller the value, the more accurate the simulation will be but more calculations will be required.
            n_time_steps (float): The number of time steps (using delta_time) for the simulation.
            tolerance_distance (float): The tolerance for the distance between _body2_ and _body1_. The simulation will stop when the distance between _body2_ and _body1_ is less than this value. It intends to avoid the simulation to continue when _body2_ is "already inside" _body1_.
            numerical_method (RungeKutta_4 | ...): The numerical method to use for the simulation.
        """
        r = self.body2.current_position + self.body2.current_velocity
        t = self.body2.current_time
        
        method_builder = ODE_METHOD[numerical_method]
        ode_function = self.body2.universe.OrbitDecay_ODE_Function(self.body1.mass, self.body2.mass, self.body2.surface_area, self.body2.atmospheric_drag_coefficient, self.body1.atmospheric_density)
        method = method_builder(ode_function, r, t)
        
        _ , values = method.List_solve_BySteps(n_time_steps, delta_time)    
        return values
    
    def trajectory_ForFinalValue(self, t_final: float, n_subdivisions: int, tolerance_distance: float , numerical_method = "RK4"):
        """Calculate the trajectory (list of tuples) of _body2_ around _body1_ using a numerical method to solve the system of differential equations associated with the trajectory.
        Args:
            t_final (float): The final time for the simulation.
            n_subdivisions (int): The number of subdivisions for the simulation. The more subdivisions, the more accurate the solution will be but more calculations will be required.
            tolerance_distance (float): The tolerance for the distance between _body2_ and _body1_. The simulation will stop when the distance between _body2_ and _body1_ is less than this value. It intends to avoid the simulation to continue when _body2_ is "already inside" _body1_.
            numerical_method (RungeKutta_4 | ...): The numerical method to use for the simulation.
        """
        r = self.body2.current_position + self.body2.current_velocity
        t = self.body2.current_time
        
        method_builder = ODE_METHOD[numerical_method]
        ode_function = self.body2.universe.OrbitDecay_ODE_Function(self.body1.mass, self.body2.mass, self.body2.surface_area, self.body2.atmospheric_drag_coefficient, self.body1.atmospheric_density)
        method = method_builder(ode_function, r, t)
        
        _ , values = method.List_solve_ForFinalValue(t_final, n_subdivisions)    
        return values
        
    def trajectory_Loop(self, delta_time: float, numerical_method = "RK4", time_delay: float = 0.0):
        """Loop through the trajectory (iterating indefinitely) of _body2_ around _body1_ using a numerical method to solve the system of differential equations associated with the trajectory. **THIS METHOD IS A LOOP SO IT DOES NOT RETURN ANYTHING AND IT WILL RUN UNTIL THE SIMULATION IS STOPPED**.      
        Args:
            delta_time (float): The time difference between each step in the simulation. The smaller the value, the more accurate the simulation will be but more calculations will be required.
            numerical_method (RungeKutta_4 | ...): The numerical method to use for the simulation.
            time_delay (float): The (artificial) time delay between each step in the simulation. For non positive values, the simulation will run as fast as possible. For positive values, the simulation will run with a delay of _time_delay_ seconds between each step.
        """
        
        r = self.body2.current_position + self.body2.current_velocity
        t = self.body2.current_time
        method_builder = ODE_METHOD[numerical_method]
        ode_function = self.body2.universe.OrbitDecay_ODE_Function(self.body1.mass, self.body2.mass, self.body2.surface_area, self.body2.atmospheric_drag_coefficient, self.body1.atmospheric_density)
        method = method_builder(ode_function, r , t)
        
        tolerance_distance = self.body1.radius
        
        if time_delay <= 0.0:
            while True:
                r[:] = sum_vectors(r, method._iteration(r, t, delta_time))
                t += delta_time
                if distance([r[0], r[1]], self.body1.current_position) < tolerance_distance:
                    break
                yield r[0], r[1]
        else:
            from time import time
            while True:
                r[:] = sum_vectors(r, method._iteration(r, t, delta_time))
                t += delta_time
                if distance([r[0], r[1]], self.body1.current_position) < tolerance_distance:
                    break
                yield r[0], r[1]
                time.sleep(time_delay)