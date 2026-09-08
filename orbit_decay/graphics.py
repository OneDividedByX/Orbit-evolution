import matplotlib.pyplot as plt
import matplotlib.animation as animation
from orbit_decay.objects import UniverseBody, Universe, UniverseInteraction
from matplotlib.figure import Figure
from matplotlib.axes import Axes

class GraphUniverse:
    def __init__(self, universe: Universe):
        """Graph a Universe object using matplotlib.
        Args:
            universe (Universe): The universe to graph.
        """
        self.universe = universe
        
    def plot_initial(self, fig: Figure, ax: Axes):
        """Initialize the plot with the initial positions of the bodies in the universe.
        Args:
            fig (Figure): The figure to plot on.
            ax (Axes): The axes to plot on.
        """
        for body in self.universe.bodies.values():
            if body.radius > 0:                
                circle = plt.Circle((body.current_position[0], body.current_position[1]), body.radius, color=body.color, alpha=0.5)
                ax.add_patch(circle)
            else:
                plt.plot(body.current_position[0], body.current_position[1], 'o', color=body.color)
        
    def _update_positions(self, body: UniverseBody, x_data: float, y_data: float, line: plt.Line2D):
        """Update the positions of a body in the universe.
        Args:
            body (UniverseBody): The body to update.
            x_data (float): The new x position of the body.
            y_data (float): The new y position of the body.
            line (plt.Line2D): The line object to update with the new positions.
        """
        body.update_position([x_data, y_data])
        line.set_data(zip(*body.list_position))
        
    def plot_loop(self, body1: UniverseBody, body2: UniverseBody , fig: Figure, ax: Axes, delta_time = 1.0):
        """Plot the trajectory of body2 around body1 following an orbit decay in a loop.

        Args:
            body1 (UniverseBody): The central body in the orbit decay.
            body2 (UniverseBody): The objective body in the orbit decay. The body which **follows** the orbit decay.
            fig (Figure): The figure to plot on.
            ax (Axes): The axes to plot on.
            delta_time (float): The time difference between each step in the simulation. The smaller the value, the more accurate the simulation will be but more calculations will be required.
        """
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
            frames = lambda: interaction.trajectory_Loop(delta_time),
            init_func = initial, 
            blit=False, 
            interval=1,
            save_count=100
        )