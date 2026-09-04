import matplotlib.pyplot as plt
import numpy as np

def rk4(r,t,h):                    
    """ Runge-Kutta 4 method """
    k1 = h*f(r,t)        
    #r es el vector de variables dependientes ,en nuestro caso (x,y,u,v) y t es la dependiente
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    return (k1 + 2*k2 + 2*k3 + k4)/6

def f(r,t):
    alpha = M*G
    beta = (C*A*rho)/m
    x,y,u,v = r[0],r[1],r[2],r[3]
    fxd = u
    fyd = v
    fud= (-alpha*(x/(((x**2)+(y**2))**1.5)))-(u*beta*(((u**2)+(v**2))**0.5))
    fvd= (-alpha*(y/(((x**2)+(y**2))**1.5)))-(v*beta*(((u**2)+(v**2))**0.5))
    return np.array([fxd, fyd, fud,fvd], float)

M=5.972*10**24 #Masa del planeta
G=6.673*10**-11 #Constante de gravitacion
C=2.2 #Constante de proporcionalidad
A=0.72 #Area del objeto que mira hacia la atmosfera
rho=7*10**-7 #Densidad de la atmosfera
m=522 #Masa del satelite
h=0.1 #Incremento

tpoints = np.arange(0, 8000, h)  
#(t_0,t_f,h)    
xpoints, ypoints ,upoints, vpoints  = [],[],[],[]
r = np.array([6830000,0,0,8000], float) #(x_0, y_0, v_{x_0}, v_{y_0})

for t in tpoints:
    xpoints.append(r[0])          
    ypoints.append(r[1])
    upoints.append(r[2]) 
    vpoints.append(r[3])
    r += rk4(r,t,h)
    
plt.grid()    
plt.plot(tpoints, xpoints)
plt.plot(tpoints, ypoints)
plt.xlabel("Tiempo segundos")
plt.ylabel("Posicion metros ")
plt.title("Decaimiento en los ejes") #Mostramos la grafica del cambio de x e y en funcion del tiempo
plt.savefig("decaimiento.png")
plt.show()
R_p=6378000 #Radio del planeta
circle1 = plt.Circle((0, 0),R_p,color='brown') #Representacion del planeta como un circulo en el plano
fig, ax = plt.subplots()
ax.add_patch(circle1)
fig.savefig('plotcircles.png') #Generamos la grafica de la trayectoria

plt.grid()
plt.xlim(-12*10**6, 12*10**6)
plt.ylim(-8*10**6, 8*10**6)
plt.xlabel("x(t) (m)")
plt.ylabel("y(t) (m)")
plt.plot(xpoints, ypoints)
plt.title("Degeneracion de la orbita del satelite",fontsize=15)
plt.show()