"""Crea una función llamada calculate() en mean_var_std.py que usa Numpy para producir la media, varianza, desviación estándar, max, min, y suma de las filas, columnas y elementos en una matriz de 3 x 3."""
import numpy as np

def calculate(list: list):
    """Recibe una lista de 9 digitos.
    Convierte la lista en una matriz de 3x3 y luego 
    devuelve un diccionario con la media, varianza,
    desviación estándar, max, min, suma a lo largo de
    ambos ejes y para la matriz aplanada.
    
    >>> calculate([0,1,2,3,4,5,6,7,8])
    {
    'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
    'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
    'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
    'max': [[6, 7, 8], [2, 5, 8], 8],
    'min': [[0, 1, 2], [0, 3, 6], 0],
    'sum': [[9, 12, 15], [3, 12, 21], 36]
    }"""
    # Conversion de lista a array y a una matriz de 3 x 3.
    array = np.array(list).reshape((3,3))
    # Calculo de la media por fila, por columna y elementos.
    mean = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)]
    # Calculo de varianza por fila, columna y elementos.
    variance = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array)]
    print(array)
    print(mean)
    print(variance)
    
    
calculate([0,1,2,3,4,5,6,7,8])