"""Funciones para calcular la sucesión de Fibonacci."""
from functools import lru_cache

def fibonacci_iterativo(n):
    if n < 0:
        raise ValueError("El índice no puede ser negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@lru_cache(maxsize=None)
def fibonacci_recursivo(n):
    if n < 0:
        raise ValueError("El índice no puede ser negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_serie(n):
    if n < 0:
        raise ValueError("El índice no puede ser negativo")
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    serie = [0, 1]
    for i in range(2, n + 1):
        serie.append(serie[i - 1] + serie[i - 2])
    return serie

def es_fibonacci(numero):
    if numero < 0:
        return False
    if numero in (0, 1):
        return True
    return es_cuadrado_perfecto(5 * numero * numero + 4) or es_cuadrado_perfecto(5 * numero * numero - 4)

def es_cuadrado_perfecto(numero):
    if numero < 0:
        return False
    raiz = int(numero ** 0.5)
    return raiz * raiz == numero
