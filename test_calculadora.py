import pytest
from src.calculadora import sumar, restar, multiplicar, dividir, raiz_cuadrada, promedio, maximo, minimo, calcular_area_rectangulo

def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_restar_con_resultado_negativo():
    # Arrange
    a, b = 3, 8
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -5

def test_multiplicar_por_cero():
    # Arrange
    a, b = 12, 0
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 0

def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act / Assert
    with pytest.raises(ValueError):
        dividir(a, b)

def test_raiz_cuadrada_de_negativo_lanza_error():
    # Arrange
    numero = -9
    # Act / Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)

def test_raiz_cuadrada_de_cero():
    # Arrange
    numero = 0
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 0

def test_promedio_lista_vacia_lanza_error():
    # Arrange
    datos = []
    # Act / Assert
    with pytest.raises(ValueError):
        promedio(datos)

def test_maximo_de_lista():
    # Arrange
    datos = [-5, -2, -9]
    # Act
    resultado = maximo(datos)
    # Assert
    assert resultado == -2

def test_minimo_lista_solo_positivos():
    # Arrange
    datos = [4, 8, 2]
    # Act
    resultado = minimo(datos)
    # Assert
    assert resultado == 2

def test_area_rectangulo():
    # Arrange
    base, altura = 5, 3
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 15

def test_dividir_normal():
    # Arrange
    a, b = 12, 3
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 4

def test_potencia():
    # Arrange
    base_num, exponente = 2, 4
    # Act
    resultado = __import__("src.calculadora", fromlist=["potencia"]).potencia(base_num, exponente)
    # Assert
    assert resultado == 16

def test_promedio_normal():
    # Arrange
    datos = [2, 4, 6]
    # Act
    resultado = promedio(datos)
    # Assert
    assert resultado == 4

def test_maximo_lista_vacia_lanza_error():
    # Arrange
    datos = []
    # Act / Assert
    with pytest.raises(ValueError):
        maximo(datos)

def test_minimo_lista_vacia_lanza_error():
    # Arrange
    datos = []
    # Act / Assert
    with pytest.raises(ValueError):
        minimo(datos)

def test_area_rectangulo_base_negativa_lanza_error():
    # Arrange
    base_num, altura = -2, 5
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base_num, altura)
