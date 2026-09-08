from time import time
from orbit_decay.constants import OrbitDecay_ODE_Function
from iterative_method import ODE_METHOD, RungeKutta_4
from linear_algebra import distance, sum_vectors

class Universe:
    bodies: dict[str, UniverseBody] = {}
    
    def __init__(self, name: str):        
        self.name = name
    @classmethod
    def register(cls, body: UniverseBody):
        cls.bodies[body.name] = body

class UniverseBody:    
    def __init__(self, universe: Universe, name: str, mass: float, radius: float, position: list[float], velocity: list[float], color: str = "b"):
        """Create a new UniverseBody object.

        Args:
            universe (Universe): The universe to which the body belongs.
            name (str): The name of the body.
            mass (float): The mass of the body in kilograms.
            radius (float): The radius of the body (m).
            position (list[float]): The initial position of the body (m).
            velocity (list[float]): The initial velocity of the body (m/s).
            color (str): The color of the body for plotting purposes.
        """
        
        self.universe = universe
        self.name = name
        self.mass = mass
        self.radius = radius
        self.initial_position = position
        self.initial_velocity = velocity
        self.color = color

        self.list_position = [self.initial_position]
        self.list_velocity = [self.initial_velocity]
        self.list_time = [0.0]
        
        universe.register(self)

    def update_position(self, new_position: list[float]):
        """Update the position of the body."""
        self.list_position.append(new_position)

    def update_velocity(self, new_velocity: list[float]):
        """Update the velocity of the body."""
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
        x = self.body2.current_position[0]
        y = self.body2.current_position[1]
        vx = self.body2.current_velocity[0]
        vy = self.body2.current_velocity[1]
        t = self.body2.current_time
        
        if numerical_method == "RK4":
            method  = RungeKutta_4(OrbitDecay_ODE_Function, [x,y,vx,vy], t)
        
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
        x = self.body2.current_position[0]
        y = self.body2.current_position[1]
        vx = self.body2.current_velocity[0]
        vy = self.body2.current_velocity[1]
        t = self.body2.current_time
        
        if numerical_method == "RK4":
            method  = RungeKutta_4(OrbitDecay_ODE_Function, [x,y,vx,vy], t)
        
        _ , values = method.List_solve_ForFinalValue(t_final, n_subdivisions)    
        return values
        
    def trajectory_Loop(self, delta_time: float, numerical_method = "RK4", time_delay: float = 0.0):
        """Loop through the trajectory (iterating indefinitely) of _body2_ around _body1_ using a numerical method to solve the system of differential equations associated with the trajectory.
        
        Args:
            delta_time (float): The time difference between each step in the simulation. The smaller the value, the more accurate the simulation will be but more calculations will be required.
            numerical_method (RungeKutta_4 | ...): The numerical method to use for the simulation.
            time_delay (float): The (artificial) time delay between each step in the simulation. For non positive values, the simulation will run as fast as possible. For positive values, the simulation will run with a delay of _time_delay_ seconds between each step.
        """
        
        r = self.body2.current_position + self.body2.current_velocity
        t = self.body2.current_time
        method_builder = ODE_METHOD[numerical_method]
        method = method_builder(OrbitDecay_ODE_Function, r , t)
        tolerance_distance = self.body1.radius
        
        if time_delay <= 0.0:
            while True:
                r[:] = sum_vectors(r, method._iteration(r, t, delta_time))
                t += delta_time
                if distance([r[0], r[1]], self.body1.current_position) < tolerance_distance:
                    break
                yield r[0], r[1]
        else:
            while True:
                r[:] = sum_vectors(r, method._iteration(r, t, delta_time))
                t += delta_time
                if distance([r[0], r[1]], self.body1.current_position) < tolerance_distance:
                    break
                yield r[0], r[1]
                time.sleep(time_delay)