# Análisis de Consumo de Recursos en Reproductor de Video

Esta aplicación permite visualizar y comparar el consumo de CPU entre dos configuraciones diferentes de un reproductor de video:

1. Sin optimización (C1(t) = t)
2. Con optimización (C2(t) = t * e^(-t))

## Requisitos

- Python 3.7 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar o descargar este repositorio
2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar el script principal:
```bash
python video_resource_analysis.py
```

El programa mostrará:
- Una gráfica comparativa de las dos funciones de consumo
- El área bajo cada curva (representando el consumo total)
- El porcentaje de reducción en el consumo de recursos
- Análisis para diferentes intervalos de tiempo

## Interpretación de Resultados

- La curva azul (C1) representa el consumo sin optimización
- La curva roja (C2) representa el consumo con optimización
- El área bajo cada curva representa el consumo total de recursos
- Una menor área indica un menor consumo total de recursos

## Características

- Visualización gráfica de las funciones de consumo
- Cálculo numérico de áreas usando integración
- Comparación de diferentes intervalos de tiempo
- Cálculo del porcentaje de reducción en el consumo 