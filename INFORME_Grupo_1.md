<div align="center">

<img src="https://raw.githubusercontent.com/MatteoRodrig/pruebas_unitarias_devops/main/capturas/logo_unal.png" alt="Logo Universidad Nacional de Colombia" width="150" />

# Universidad Nacional de Colombia

### Sede Manizales — Administración de Sistemas Informáticos

---

# Taller — Análisis y Mejora de Pruebas Unitarias

**Curso:** Introducción a DevOps  
**Docente:** César Augusto Palacios Alarcón

---

**Estudiante:** Daniela Fernanda Mendoza Epia  
**Grupo:** 1  
**Fecha de entrega:** 17 de octubre de 2026

---

</div>

## Tabla de contenido

1. [Introducción](#1-introducción)
2. [Análisis por módulo](#2-análisis-por-módulo)
3. [Tabla de bugs corregidos](#3-tabla-de-bugs-corregidos)
4. [Resultados y cobertura](#4-resultados-y-cobertura)
5. [Evidencias visuales de referencia](#5-evidencias-visuales-de-referencia)
6. [Reflexión final](#6-reflexión-final)

---

## 1. Introducción

Este informe describe el trabajo realizado en el taller de análisis y mejora de pruebas unitarias de la asignatura Introducción a DevOps. El objetivo es utilizar pruebas automatizadas para revisar el comportamiento de funciones, detectar errores, validar casos límite y medir qué parte del código ejecutan las pruebas.

Para organizar los casos se utiliza la estructura AAA (*Arrange, Act, Assert*): preparar los datos, ejecutar la función y comprobar que el resultado sea el esperado. El trabajo se concentra en tres módulos: `calculadora`, `descuentos` y `fibonacci`.

## 2. Análisis por módulo

### 2.1. Módulo `calculadora`

Este módulo contiene operaciones matemáticas básicas. Las pruebas revisan operaciones normales y situaciones que requieren validación, como dividir por cero, calcular la raíz cuadrada de un número negativo y trabajar con listas vacías al obtener promedios, máximos o mínimos.

Se incluyen casos límite porque ayudan a encontrar errores que no siempre aparecen con entradas comunes. Por ejemplo, una función que calcula el mínimo debe devolver un valor que realmente pertenezca a la lista y la raíz cuadrada debe manejar correctamente las entradas negativas dentro del dominio de los números reales.

### 2.2. Módulo `descuentos`

Este módulo calcula descuentos y precios finales. Las pruebas consideran descuentos de 0 % y 100 %, montos descontados, impuestos, precios negativos, descuentos por volumen y descuentos acumulados o apilados.

Estos casos son importantes porque el orden de las operaciones afecta el precio final. También se revisan los límites de los porcentajes para evitar resultados inválidos o comportamientos inesperados.

### 2.3. Módulo `fibonacci`

Este módulo contiene funciones relacionadas con la sucesión de Fibonacci. Se prueban índices cero y negativos, términos conocidos, generación de la serie, comprobación de pertenencia a Fibonacci y detección de cuadrados perfectos.

También se utiliza memoización en la versión recursiva para reutilizar resultados ya calculados y evitar repetir innecesariamente el mismo trabajo. Los casos límite permiten verificar que las funciones respondan de manera controlada ante entradas que no son válidas.

## 3. Tabla de bugs corregidos

| Función | Entrada que revela el problema | Comportamiento incorrecto identificado | Comportamiento esperado / corrección |
|---|---|---|---|
| `raiz_cuadrada` | `-9` | Puede producir un resultado complejo en vez de rechazar la entrada | Validar el número y lanzar `ValueError` si es negativo |
| `minimo` | `[4, 8, 2]` | Inicializar el mínimo en cero puede devolver `0`, aunque no esté en la lista | Inicializar con un elemento de la lista o utilizar una estrategia equivalente correcta |
| `calcular_precio_final` | Precio 100, impuesto 10 %, descuento 20 % | Calcular el impuesto sobre el precio original produce un precio final incorrecto | Aplicar primero el descuento y calcular el impuesto sobre el precio descontado |
| `descuento_apilado` | Precio 100, descuentos `[60, 50]` | La suma de porcentajes puede superar el 100 % y generar un manejo poco claro del caso | Validar explícitamente el porcentaje acumulado y aplicar la regla definida por la función |

## 4. Resultados y cobertura

La ejecución registrada en `RESULTADO_PRUEBAS.txt` reporta **44 pruebas aprobadas** y una cobertura global del **85 %**.

| Módulo | Sentencias no cubiertas | Cobertura | Estado frente a una meta del 85 % |
|---|---:|---:|---|
| `calculadora.py` | 3 | 92 % | Cumple |
| `descuentos.py` | 12 | 80 % | Aún no cumple; requiere más pruebas |
| `fibonacci.py` | 6 | 86 % | Cumple |
| **Total** | **21** | **85 %** | Cobertura global alcanzada |

Aunque la cobertura global llega al 85 %, el módulo `descuentos.py` tiene 80 %. Por eso, no se debe afirmar que todos los módulos alcanzan el mínimo del 85 %. Para mejorar este resultado se recomienda agregar pruebas que cubran las líneas que aparecen como no ejecutadas en el reporte: 7, 12, 19, 21, 23, 30, 32, 37, 39, 48, 54 y 60 de `descuentos.py`.

Para volver a ejecutar las pruebas y generar un reporte actualizado, se puede usar:

```bash
python -m pytest tests/ -v --cov=src.calculadora --cov=src.descuentos --cov=src.fibonacci --cov-report=term-missing
```

La salida más reciente debe conservarse en `RESULTADO_PRUEBAS.txt` para que los resultados descritos en este informe se puedan verificar.

## 5. Evidencias visuales de referencia

Las siguientes imágenes están enlazadas desde el repositorio usado como referencia para el formato del informe. Ilustran ejemplos de ejecución de pruebas en los módulos de calculadora y descuentos, pero **no son capturas de una ejecución propia del Grupo 1**. La evidencia de nuestros resultados es el archivo `RESULTADO_PRUEBAS.txt`; si el docente exige capturas propias, deben tomarse ejecutando las pruebas de este repositorio.

### 5.1. Ejemplos de pruebas para calculadora

**Prueba inicial y detección de un error (referencia):**

![Captura de referencia: prueba inicial de calculadora](https://raw.githubusercontent.com/MatteoRodrig/pruebas_unitarias_devops/main/capturas/Cap1.png)

![Captura de referencia: prueba que revela un error en calculadora](https://raw.githubusercontent.com/MatteoRodrig/pruebas_unitarias_devops/main/capturas/Cap2error_1.png)

**Ejecución de pruebas después de corregir el error (referencia):**

![Captura de referencia: pruebas de calculadora aprobadas](https://raw.githubusercontent.com/MatteoRodrig/pruebas_unitarias_devops/main/capturas/Cap3.png)

### 5.2. Ejemplos de pruebas para descuentos

![Captura de referencia: pruebas de descuentos que revelan errores](https://raw.githubusercontent.com/MatteoRodrig/pruebas_unitarias_devops/main/capturas/Cap4error_2.png)

![Captura de referencia: pruebas de descuentos aprobadas](https://raw.githubusercontent.com/MatteoRodrig/pruebas_unitarias_devops/main/capturas/Cap5.png)

**Fuente de las imágenes de referencia:** [repositorio de referencia de MatteoRodrig](https://github.com/MatteoRodrig/pruebas_unitarias_devops/tree/main/capturas). Se recomienda reemplazarlas o complementarlas con capturas propias antes de entregar si la guía exige evidencia directa del trabajo del grupo.

## 6. Reflexión final

Las pruebas unitarias permiten comprobar el comportamiento de las funciones tanto con entradas normales como con valores límite y entradas inválidas. La estructura AAA ayuda a separar la preparación de los datos, la ejecución y la comprobación del resultado, por lo que las pruebas son más fáciles de leer y mantener.

La cobertura indica qué parte del código fue ejecutada durante las pruebas, pero no garantiza por sí sola que el programa esté libre de errores. Por eso también es importante elegir casos significativos y comprobar los resultados esperados. En esta ejecución se aprobaron 44 pruebas y se alcanzó un 85 % de cobertura global; sin embargo, todavía hace falta ampliar las pruebas del módulo `descuentos` para llegar al 85 % en ese archivo.

El taller permite observar que las pruebas automatizadas son una parte importante del proceso de desarrollo: ayudan a detectar problemas, comprobar correcciones y reducir el riesgo de que un cambio dañe funcionalidades que ya servían.

---

<div align="center">

**Fin del informe — Grupo 1**

</div>
