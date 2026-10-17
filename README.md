# 🎯 PROYECTO: PRUEBAS UNITARIAS - GRUPO 1

## 📌 Descripción

Este proyecto corresponde al taller de pruebas unitarias de la asignatura. Su propósito es practicar la identificación de errores, la validación del comportamiento de funciones y la ejecución de pruebas automatizadas con **Python** y **pytest**.

El repositorio contiene el código fuente, los archivos de pruebas y los recursos necesarios para ejecutar el proyecto.

## 🎯 Objetivos

- Comprender la importancia de las pruebas unitarias en el desarrollo de software.
- Verificar que las funciones produzcan los resultados esperados.
- Identificar errores y casos límite.
- Ejecutar pruebas automatizadas y revisar sus resultados.
- Analizar la cobertura de las pruebas cuando la herramienta esté configurada.

## 📂 Estructura del repositorio

```text
pruebas_unitarias_devops/
├── src/                 # Código fuente del proyecto
├── tests/               # Pruebas unitarias
├── README.md            # Documentación del proyecto
├── requirements.txt     # Dependencias de Python
└── setup.sh             # Script de configuración, si se utiliza
```

> La estructura puede variar según los archivos que se hayan agregado durante el desarrollo del taller.

## 🛠️ Requisitos

- Python 3 instalado.
- Git, para clonar el repositorio.
- `pip`, para instalar las dependencias.

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/dmendozaep-code/pruebas_unitarias_devops.git
cd pruebas_unitarias_devops
```

### 2. Crear un entorno virtual (recomendado)

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

En Linux o macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Si `pytest` no quedó instalado mediante las dependencias, se puede instalar con:

```bash
pip install pytest pytest-cov
```

### 4. Ejecutar las pruebas

Desde la carpeta principal del proyecto, ejecutar:

```bash
pytest
```

Para obtener un resumen más detallado:

```bash
pytest -v
```

### 5. Revisar la cobertura (si `pytest-cov` está instalado)

```bash
pytest --cov=src --cov-report=term-missing
```

Para generar un reporte HTML:

```bash
pytest --cov=src --cov-report=html
```

El reporte HTML se guarda en la carpeta `htmlcov/`. Para consultarlo, abrir el archivo `htmlcov/index.html` en el navegador.

## 🧪 Aspectos evaluados en el taller

Durante el desarrollo se pueden abordar los siguientes aspectos:

1. **Detección de errores:** encontrar comportamientos incorrectos en el código.
2. **Diseño de pruebas:** comprobar los resultados esperados mediante aserciones.
3. **Casos límite:** validar entradas vacías, valores extremos y datos no válidos cuando corresponda.
4. **Cobertura:** identificar qué partes del código ejecutan las pruebas y qué líneas necesitan más validación.

## 📄 Evidencias y resultados

Los resultados deben registrarse con base en la ejecución real de las pruebas. Para evitar presentar datos incorrectos, el número de pruebas aprobadas, los errores encontrados y el porcentaje de cobertura se deben completar después de ejecutar los comandos en el entorno del proyecto.

## 👥 Integrantes

**Grupo 1**

Agregar aquí los nombres de los integrantes del grupo, de acuerdo con las indicaciones del taller.

## 🔗 Repositorio

[Pruebas unitarias DevOps - Grupo 1](https://github.com/dmendozaep-code/pruebas_unitarias_devops)

---

*Documentación del proyecto académico de pruebas unitarias con Python y pytest.*
