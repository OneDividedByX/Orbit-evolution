<header>
    <h1>Orbit Decay Simulation</h1>
</header>
<div>
    <p>
        Simulate the orbit decay of a satellite around a central body using a numerical method (Runge-Kutta 4th order as preferred) to solve the system of ordinary differential equations associated with it.
    </p>
    <p>
        Currently working in a bidimensional (2D) space. Specifically, the associated ODE system is defined as follows:
    </p>
    $$
    r''(t)= -\dfrac{GM}{\|r(t)\|^3}r(t)-k\|r'(t)\|r'(t)
    $$
    <p>
        where $r(t)$ and $r'(t)$ are (respectively) the position and velocity vectors of the satellite, $M$ is the mass of the central body, $G$ is the gravitational constant and
    </p>
    $$
    k=\frac{CA\rho}{m}
    $$
    is a constant that depends on the satellite's mass $m$, satellite's surface area $A$, drag coefficient $C$ and the fluid density $\rho$ of the environment which the satellite is moving through.
</div>