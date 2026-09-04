from linear_algebra import sum_vectors, mult_scalar

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