"""Crea una función llamada calculate() en mean_var_std.py que usa Numpy para producir la media, varianza, desviación estándar, max, min, y suma de las filas, columnas y elementos en una matriz de 3 x 3."""
import numpy as np

def calculate(list: list):
    """Recibe una lista de 9 digitos.
    Convierte la lista en una matriz de 3x3 y luego 
    devuelve un diccionario con la media, varianza,
    desviación estándar, max, min, suma a lo largo de
    ambos ejes y para la matriz aplanada."""

    # Conversion de lista a array y a una matriz de 3 x 3.
    array = np.array(list).reshape((3,3))
    # Calculo de la media por fila, por columna y elementos.
    mean = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)]
    # Calculo de varianza por fila, columna y elementos.
    variance = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array)]
    # Calculo desviación estándar.
    standard_deviation = [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array)]
    # Calculo maximos
    calc_max = [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array)]
    # Calculo minimos
    calc_min = [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array)]
    print(array)
    print(mean)
    print(variance)
    print(standard_deviation)
    print(calc_max)
    print(calc_min)
    
calculate([0,1,2,3,4,5,6,7,8])