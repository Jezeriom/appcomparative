import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import matplotlib.patches as patches

def c1(t):
    """Función de consumo sin optimización: C1(t) = t"""
    return t

def c2(t):
    """Función de consumo con optimización: C2(t) = t * e^(-t)"""
    return t * np.exp(-t)

def calculate_area(func, a, b):
    """Calcula el área bajo la curva usando integración numérica"""
    result, _ = integrate.quad(func, a, b)
    return result

def plot_consumption_comparison(t_start=0, t_end=5):
    """Genera y muestra la gráfica comparativa de consumo de CPU"""
    # Crear puntos para la gráfica
    t = np.linspace(t_start, t_end, 1000)
    y1 = c1(t)
    y2 = c2(t)
    
    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Graficar las funciones
    ax.plot(t, y1, 'b-', label='Sin optimización (C1(t) = t)', linewidth=2)
    ax.plot(t, y2, 'r-', label='Con optimización (C2(t) = t*e^(-t))', linewidth=2)
    
    # Calcular áreas
    area1 = calculate_area(c1, t_start, t_end)
    area2 = calculate_area(c2, t_start, t_end)
    
    # Agregar área sombreada
    ax.fill_between(t, y1, alpha=0.2, color='blue')
    ax.fill_between(t, y2, alpha=0.2, color='red')
    
    # Configurar la gráfica
    ax.set_xlabel('Tiempo (t)', fontsize=12)
    ax.set_ylabel('Consumo de CPU', fontsize=12)
    ax.set_title('Comparación de Consumo de CPU en Reproductor de Video', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(fontsize=10)
    
    # Agregar información de áreas
    info_text = f'Área sin optimización: {area1:.2f}\nÁrea con optimización: {area2:.2f}\nReducción: {((area1-area2)/area1*100):.1f}%'
    ax.text(0.02, 0.98, info_text, transform=ax.transAxes, 
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()

def main():
    print("Análisis de Consumo de Recursos en Reproductor de Video")
    print("=" * 50)
    
    # Calcular y mostrar áreas para diferentes intervalos
    intervals = [(0, 5), (0, 10), (0, 15)]
    
    for start, end in intervals:
        print(f"\nIntervalo de tiempo [{start}, {end}]:")
        area1 = calculate_area(c1, start, end)
        area2 = calculate_area(c2, start, end)
        reduction = ((area1 - area2) / area1) * 100
        
        print(f"Área sin optimización: {area1:.2f}")
        print(f"Área con optimización: {area2:.2f}")
        print(f"Reducción de consumo: {reduction:.1f}%")
    
    # Mostrar gráfica comparativa
    plot_consumption_comparison()

if __name__ == "__main__":
    main() 