# Informe — Análisis y mejora de pruebas unitarias

## 1. Datos
- **Estudiante:** Daniela Fernanda Mendoza Epia
- **Grupo:** Por completar
- **Asignatura:** Introducción a DevOps
- **Fecha:** 17 de octubre de 2026

## 2. Análisis por módulo

### Calculadora
Se probaron operaciones básicas, división por cero, raíz cuadrada de un número negativo, promedio de una lista vacía, máximos y mínimos. Los casos límite se eligieron para detectar errores de validación y de inicialización de valores.

### Descuentos
Se probaron descuentos de 0 % y 100 %, cálculo del monto descontado, impuesto después del descuento, precios negativos, descuento por volumen y descuentos acumulados/apilados. Estos casos comprueban límites porcentuales y el orden de las operaciones.

### Fibonacci
Se probaron índices cero y negativos, un término conocido de la serie, generación de una serie, pertenencia a Fibonacci y detección de cuadrados perfectos. Se agregó memoización a la versión recursiva para evitar repetir cálculos.

## 3. Tabla de bugs corregidos

| Función | Entrada que revela el bug | Resultado erróneo | Resultado esperado | Corrección |
|---|---|---|---|---|
| `raiz_cuadrada` | `-9` | Devuelve un resultado complejo en vez de rechazar la entrada | `ValueError` para números negativos en el dominio real | Validar que el número no sea negativo antes de calcular |
| `minimo` | `[4, 8, 2]` | Devuelve `0` porque inicializaba el mínimo en cero | `2` | Inicializar usando el primer elemento o `min(lista)` |
| `calcular_precio_final` | precio 100, impuesto 10 %, descuento 20 % | Calcula el impuesto sobre 100 y devuelve 90 | 88, aplicando 10 % de impuesto sobre 80 | Calcular el impuesto sobre el precio descontado |
| `descuento_apilado` | precio 100, descuentos `[60, 50]` | El porcentaje total supera el 100 % y termina siendo rechazado indirectamente | Rechazo explícito y comprensible | Validar que la suma no supere 100 % |

## 4. Cobertura

Ejecutar en el entorno del proyecto:

```bash
python -m pytest tests/ -v --cov=src.calculadora --cov=src.descuentos --cov=src.fibonacci --cov-report=term-missing
```

**Resultado medido en este entorno:** se ejecutaron las pruebas con `pytest` y `pytest-cov`. Consulta `RESULTADO_PRUEBAS.txt` para la salida completa y los porcentajes por módulo. La cobertura debe alcanzar al menos 85 % en los módulos trabajados; si el resultado queda por debajo, agrega casos para las líneas marcadas como no cubiertas y vuelve a ejecutar el comando.

## 5. Reflexión final

Las pruebas unitarias permiten comprobar el comportamiento de funciones con entradas normales y con casos límite. La estructura AAA ayuda a separar la preparación de los datos, la ejecución de la función y la comprobación del resultado, lo que hace que las pruebas sean más fáciles de leer.

La cobertura indica qué parte del código se ejecutó durante las pruebas, pero no demuestra por sí sola que el programa esté libre de errores. Es posible ejecutar una línea sin comprobar todos sus resultados posibles. Por eso se deben diseñar pruebas con resultados esperados claros, valores límite y entradas inválidas.

Durante este ejercicio se observa que errores pequeños, como inicializar incorrectamente una variable o aplicar un impuesto sobre una base equivocada, pueden cambiar el resultado. Las pruebas automatizadas permiten detectar estos problemas antes de integrar los cambios y facilitan verificar que las correcciones sigan funcionando.
