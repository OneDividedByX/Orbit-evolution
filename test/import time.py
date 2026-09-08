import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. GENERADOR: Calcula valores indefinidamente y los "entrega" uno a uno
def generador_valores():
    x = 0.0
    while True:
        # Aquí va tu ecuación o cálculo matemático
        # Como ejemplo, calculamos el seno de x
        y = np.sin(x)
        
        # 'yield' pausa la función, entrega los valores y espera el siguiente ciclo
        yield x, y  
        
        x += 0.1
        time.sleep(0.05) # Simula un pequeño retraso de cómputo

# 2. CONFIGURACIÓN DE MATPLOTLIB
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-', lw=2) # Línea roja para el gráfico

# Listas para almacenar el historial de datos acumulados
x_data, y_data = [], []

def inicializar_grafico():
    """Configura los límites iniciales del gráfico."""
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("Tiempo / X")
    ax.set_ylabel("Valor Calculado")
    ax.set_title("Cálculo Matemático en Tiempo Real")
    return line,

# 3. FUNCIÓN DE ACTUALIZACIÓN: Se ejecuta cada vez que el generador produce un valor
def actualizar_grafico(datos_nuevos):
    x_nuevo, y_nuevo = datos_nuevos
    
    # Almacenamos el nuevo valor en nuestro historial
    x_data.append(x_nuevo)
    y_data.append(y_nuevo)
    
    # Actualizamos los datos de la línea en el gráfico
    line.set_data(x_data, y_data)
    
    # Ajuste dinámico del eje X si los datos se salen de la pantalla (efecto scroll)
    if x_nuevo > ax.get_xlim()[1]:
        ax.set_xlim(x_data[0], x_nuevo + 5)
        ax.figure.canvas.draw()
        
    return line,

# 4. CREACIÓN DE LA ANIMACIÓN
# FuncAnimation se encarga de llamar al generador y pasarle los datos a 'actualizar_grafico'
ani = animation.FuncAnimation(
    fig, 
    actualizar_grafico, 
    frames=generador_valores, # Nuestra función indefinida
    init_func=inicializar_grafico, 
    blit=True, 
    interval=1, # Tiempo en milisegundos entre actualizaciones
    save_count=100 # Evita advertencias de memoria reteniendo los últimos 100 frames
)

plt.show()
