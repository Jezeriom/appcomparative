from flask import Flask, render_template, jsonify
import time
import psutil
import random
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Variables globales para almacenar el historial de consumo
consumption_history1 = []
consumption_history2 = []
time_history = []
start_time = time.time()

def calculate_consumption(time_elapsed, is_optimized=False):
    """Calcula el consumo de CPU basado en el tiempo transcurrido."""
    if is_optimized:
        # Modelo optimizado: consumo más bajo y estable
        base = 0.2
        amplitude = 0.1
        frequency = 0.5
    else:
        # Modelo no optimizado: consumo más alto y variable
        base = 0.4
        amplitude = 0.2
        frequency = 1.0
    
    # Añadir variación aleatoria para simular fluctuaciones reales
    noise = random.uniform(-0.05, 0.05)
    
    # Calcular el consumo usando una función sinusoidal con ruido
    consumption = base + amplitude * np.sin(2 * np.pi * frequency * time_elapsed) + noise
    
    # Asegurar que el consumo esté entre 0 y 1
    return max(0, min(1, consumption))

def calculate_area(consumption_history):
    """Calcula el área bajo la curva de consumo."""
    if len(consumption_history) < 2:
        return 0
    
    # Usar la regla del trapecio para calcular el área
    return np.trapezoid(consumption_history, dx=1.5)  # dx=1.5 porque actualizamos cada 1.5 segundos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_consumption_data')
def get_consumption_data():
    global consumption_history1, consumption_history2, time_history, start_time
    
    # Calcular tiempo transcurrido
    current_time = time.time()
    time_elapsed = current_time - start_time
    
    # Calcular consumo actual
    consumption1 = calculate_consumption(time_elapsed, False)
    consumption2 = calculate_consumption(time_elapsed, True)
    
    # Actualizar historiales
    consumption_history1.append(consumption1)
    consumption_history2.append(consumption2)
    time_history.append(time_elapsed)
    
    # Mantener solo los últimos 30 puntos (5 minutos con actualización cada 5 segundos)
    if len(consumption_history1) > 30:
        consumption_history1.pop(0)
        consumption_history2.pop(0)
        time_history.pop(0)
    
    # Calcular áreas
    area1 = calculate_area(consumption_history1)
    area2 = calculate_area(consumption_history2)
    
    # Solo consumo simulado, no real
    return jsonify({
        'time': time_elapsed,
        'consumption1': consumption1,
        'consumption2': consumption2,
        'area1': area1,
        'area2': area2,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })

if __name__ == '__main__':
    app.run(debug=True) 