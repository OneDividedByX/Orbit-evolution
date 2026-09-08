import matplotlib.pyplot as plt
import matplotlib.animation as animation
from orbit_decay.objects import UniverseBody, Universe, UniverseInteraction
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
        line.set_data(zip(*body.list_position))
        
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
            blit=False, 
            interval=1, # Tiempo en milisegundos entre actualizaciones
            save_count=100 # Evita advertencias de memoria reteniendo los últimos 100 frames
        )