import pytest
from src.fibonacci import fibonacci_iterativo, fibonacci_recursivo, fibonacci_serie, es_fibonacci, es_cuadrado_perfecto

def test_fibonacci_iterativo_cero():
    # Arrange
    n = 0
    # Act
    resultado = fibonacci_iterativo(n)
    # Assert
    assert resultado == 0

def test_fibonacci_iterativo_septimo():
    # Arrange
    n = 7
    # Act
    resultado = fibonacci_iterativo(n)
    # Assert
    assert resultado == 13

def test_fibonacci_recursivo_indice_negativo():
    # Arrange
    n = -1
    # Act / Assert
    with pytest.raises(ValueError):
        fibonacci_recursivo(n)

def test_fibonacci_serie_hasta_cinco():
    # Arrange
    n = 5
    # Act
    resultado = fibonacci_serie(n)
    # Assert
    assert resultado == [0, 1, 1, 2, 3, 5]

def test_es_fibonacci_numero_valido():
    # Arrange
    numero = 21
    # Act
    resultado = es_fibonacci(numero)
    # Assert
    assert resultado is True

def test_es_fibonacci_numero_no_valido():
    # Arrange
    numero = 22
    # Act
    resultado = es_fibonacci(numero)
    # Assert
    assert resultado is False

def test_cuadrado_perfecto_negativo():
    # Arrange
    numero = -4
    # Act
    resultado = es_cuadrado_perfecto(numero)
    # Assert
    assert resultado is False

def test_fibonacci_iterativo_negativo():
    # Arrange
    n = -3
    # Act / Assert
    with pytest.raises(ValueError):
        fibonacci_iterativo(n)

def test_fibonacci_recursivo_caso_base_uno():
    # Arrange
    n = 1
    # Act
    resultado = fibonacci_recursivo(n)
    # Assert
    assert resultado == 1

def test_fibonacci_serie_cero():
    # Arrange
    n = 0
    # Act
    resultado = fibonacci_serie(n)
    # Assert
    assert resultado == [0]

def test_fibonacci_serie_negativo():
    # Arrange
    n = -1
    # Act / Assert
    with pytest.raises(ValueError):
        fibonacci_serie(n)

def test_cuadrado_perfecto_positivo():
    # Arrange
    numero = 25
    # Act
    resultado = es_cuadrado_perfecto(numero)
    # Assert
    assert resultado is True
