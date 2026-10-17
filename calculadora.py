"""Módulo de calculadora con validaciones corregidas."""
import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No existe raíz cuadrada real para un número negativo")
    return math.sqrt(numero)

def promedio(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return sum(lista) / len(lista)

def maximo(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return max(lista)

def minimo(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return min(lista)

def calcular_area_rectangulo(base, altura):
    if base < 0 or altura < 0:
        raise ValueError("La base y altura no pueden ser negativas")
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    if base < 0 or altura < 0:
        raise ValueError("La base y altura no pueden ser negativas")
    return 2 * (base + altura)
