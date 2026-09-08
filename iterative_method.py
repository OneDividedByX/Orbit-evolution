from linear_algebra import sum_vectors, mult_scalar
from typing import Callable

def rk4(r, t, h,func_constants):
    """ Runge-Kutta 4 method """
    k1 = mult_scalar(h, f(r, t, func_constants)) #h*f(r, t, func_constants)        #r es el vector de variables dependientes ,en nuestro caso (x,y,u,v) y t es la independiente
    k2 = mult_scalar(h, f(sum_vectors(r, mult_scalar(0.5, k1)), t + 0.5 * h, func_constants))
    k3 = mult_scalar(h, f(sum_vectors(r, mult_scalar(0.5, k2)), t + 0.5 * h, func_constants))
    k4 = mult_scalar(h, f(sum_vectors(r, k3), t + h, func_constants))
    return sum_vectors(mult_scalar(1/6, k1), sum_vectors(mult_scalar(2/6, k2), sum_vectors(mult_scalar(2/6, k3), mult_scalar(1/6, k4))))

def f(r, t, func_constants):
    M,m,G,C,A,rho=func_constants[0],func_constants[1],func_constants[2],func_constants[3],func_constants[4],func_constants[5]
    alpha = M*G #M*G
    beta = (C*A*rho)/m  #10^-14
    x, y,u,v = r[0], r[1],r[2],r[3]
    fxd = u
    fyd = v
    fud= (-alpha*(x/(((x**2)+(y**2))**1.5)))-(u*beta*(((u**2)+(v**2))**0.5))
    fvd= (-alpha*(y/(((x**2)+(y**2))**1.5)))-(v*beta*(((u**2)+(v**2))**0.5))
    return [fxd, fyd, fud, fvd]

ODE_Method = {'rk4': rk4, 'f': f}

class RungeKutta_4:
    def __init__(self, function: Callable[[list[float], float], list[float]], r_0: list[float], t_0: float):
        """Numerical method for solving ordinary differential equations using the Runge-Kutta 4th order method.
        Args:
            function (Callable[[list[float], float], list[float]]): The function _f_ representing the system of differential equations _f(r, t)=0_, _r = r(t)_.
            r_0 (list[float]): The initial values of the dependent variables.
            t_0 (float): The initial value of the independent variable.
            h (float): The step size of the independent variable for the numerical integration.
        """
        self.r_0 = r_0
        self.t_0 = t_0
        self.function = function
        
    def _iteration(self, r: list[float], t: float, h: float):
        """Perform a single iteration of the Runge-Kutta 4th order method."""
        k1 = mult_scalar(h, self.function(r, t))
        k2 = mult_scalar(h, self.function(sum_vectors(r, mult_scalar(0.5, k1)), t + 0.5 * h))
        k3 = mult_scalar(h, self.function(sum_vectors(r, mult_scalar(0.5, k2)), t + 0.5 * h))
        k4 = mult_scalar(h, self.function(sum_vectors(r, k3), t + h))
        return sum_vectors(mult_scalar(1/6, k1), sum_vectors(mult_scalar(2/6, k2), sum_vectors(mult_scalar(2/6, k3), mult_scalar(1/6, k4))))
    
    def solve_BySteps(self, n_steps: int, h: float):
        """Solve the system of differential equations using the Runge-Kutta 4th order method after a specified number of steps given a step size.
        Args:
            n_steps (int): The number of steps to perform.
            h (float): The step size of the independent variable for the numerical integration. The smaller the value, the more accurate the simulation will be but more calculations will be required.
        """
        r = self.r_0.copy()
        t = self.t_0
        for _ in range(n_steps):
            r = self._iteration(r, t, h)
            t += h
        return r
    
    def List_solve_BySteps(self, n_steps: int, h: float):
        """Solve the system of differential equations using the Runge-Kutta 4th order method after a specified number of steps given a step size and store the obtained values for each step in a list.
        Args:
            n_steps (int): The number of steps to perform.
            h (float): The step size of the independent variable for the numerical integration. The smaller the value, the more accurate the simulation will be but more calculations will be required.
        """
        r = self.r_0.copy()
        t = self.t_0
        values = [(r, t)]
        for _ in range(n_steps):
            r = self._iteration(r, t, h)
            t += h
            values.append((r, t))
        return r, values
    
    def solve_ForFinalValue(self, t_final: float, n_subdivisions: int):
        """Solve the system of differential equations using the Runge-Kutta 4th order method until a specified final value of the independent variable is reached.
        Args:
            t_final (float): The final value of the independent variable to reach.
            n_subdivisions (int): The number of subdivisions to use for the numerical integration. The more subdivisions, the more accurate the solution will be but more calculations will be required.
        """
        if n_subdivisions <= 0:
            n_subdivisions = 1
        h = float((t_final - self.t_0) / n_subdivisions)
    
        return self.solve_BySteps(n_subdivisions, h)
    
    def List_solve_ForFinalValue(self, t_final: float, n_subdivisions: int):
        """Solve the system of differential equations using the Runge-Kutta 4th order method until a specified final value of the independent variable is reached and store the obtained values for each step in a list.
        Args:
            t_final (float): The final value of the independent variable to reach.
            n_subdivisions (int): The number of subdivisions to use for the numerical integration. The more subdivisions, the more accurate the solution will be but more calculations will be required.
        """
        if n_subdivisions <= 0:
            n_subdivisions = 1
        h = float((t_final - self.t_0) / n_subdivisions)
    
        return self.List_solve_BySteps(n_subdivisions, h)
            