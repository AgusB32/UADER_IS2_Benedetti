# Gestión de Configuración y Programación Python - UADER_IS2_{Benedetti}

## Propósito del Repositorio
Este repositorio contiene materiales y ejercicios prácticos para la gestión de configuración usando Git/GitHub y programación en Python, como parte de la asignatura Ingeniería de Software II.

### Estructura de Carpetas
├── src/ # Códigos fuente (ej: primos.py)
├── doc/ # Documentación relacionada
├── bin/ # Archivos binarios/ejecutables
└── script/ # Scripts auxiliares


## Instalación Requerida
1. **Software Obligatorio** (lista ordenada):
   - Git ([descarga](https://git-scm.com/))
   - Python 3 + Pip3 ([python.org](https://www.python.org/downloads/))

2. **Pasos de Configuración** (lista numerada):
   1. Crear cuenta en GitHub.
   2. Clonar este repositorio.
   3. Ejecutar `python3 src/primos.py` para verificar funcionamiento.

### Ejemplo de Uso
```python
# En src/primos.py
def es_primo(num):
    """Función que verifica si un número es primo"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
