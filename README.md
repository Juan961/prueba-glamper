
# Glamper - Cuerpos de agua

Solución a la prueba propuesta por Glamper

## 📋 Descripción del problema

Un cartógrafo lo ha llamado a usted para que lo ayude a programar un sistema que le permita encontrar los cuerpos de agua más grandes dentro de cualquier terreno de tamaño arbitrario. Los terrenos vienen codificados en tablas de la siguiente manera: 

![Alt text](/assets/gampler-ejemplo.png?raw=true)

El cartógrafo le indica a usted que, debido a las características de los terrenos a analizar, todo lo que esté por debajo de 0 se considera agua, y el resto es terreno, como se puede apreciar el ejemplo anterior. 
Para el ejemplo anterior, los cuerpos de agua que existen, organizados por área (asumiendo que cada celda del mapa mide 1 m2), son:

1. 4 m2
2. 2 m2

Con base en la información dada, desarrolle un sistema en Python que pueda ejecutar las siguientes tareas:
1. Generar mapas arbitrarios de 1000 x 1000, para poder evaluar la correcta ejecución del programa.
2. Identificar los cuerpos de agua presentes en un mapa dado de n x n, y organizarlos por área estimada. Se puede asumir que cada celda mide 1 m2 para la estimación de área de cada cuerpo de agua.

## 🚀 Start
Inicie la aplicación usando el comando 

```
python main.py
```

Aparecerá un menú en la consola con la cual podrá: 
1. Generar una matriz de 1000x1000
2. Generar una matriz de n x n
3. Generar la matriz de ejemplo (Imagen)
4. Salir de la aplicación

## ❓ ¿Cómo funciona?

La aplicación genera una matriz n x n (n se escoge de manera aleatoria), luego se rellena con valores entre 5 y -5, posteriormente cuando el usuario lo indique el algoritmo comienza a iterar el arreglo para buscar celdas donde el valor sea menor a 0, si así lo es entonces buscará alrededor de esa celda para estimar el área total donde los valores son menores que 0.

