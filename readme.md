# Orbit Decay Simulation
Simulate the orbit decay of a satellite around a central body using a numerical method (Runge-Kutta 4th order as preferred) to solve the system of ordinary differential equations associated with it.

Currently working in a bidimensional (2D) space. Specifically, the associated ODE system is defined as follows:

$$
r''(t)= -\dfrac{GM}{\|r(t)\|^3}r(t)-k\|r'(t)\|r'(t)
$$

Where $r(t)$ and $r'(t)$ are (respectively) the position ([m]) and velocity ([m/s]) vectors of the satellite, $M$ is the mass of the central body (kg), $G$ is the gravitational constant and:

$$
k=\frac{CA\rho}{m}
$$

This is a constant that depends on the satellite's mass $m$ (kg), satellite's surface area $A$ (m²), drag coefficient $C$, and the fluid density $\rho$ (kg/m³) of the environment which the satellite is moving through.