#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función para calcular el factorial de un número
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Función para calcular los factoriales en un rango dado
def calcular_factoriales(desde, hasta):
    for num in range(desde, hasta + 1):
        print(f"Factorial {num}! es {factorial(num)}")

# Verifica si se pasó un argumento en la línea de comandos, de lo contrario, solicita entrada al usuario
if len(sys.argv) < 2:
    entrada = input("Ingrese un rango (ej. 4-8, -10, 5- o -60): ")
else:
    entrada = sys.argv[1]

try:
    # Procesa la entrada para aceptar diferentes formatos de rango
    if "-" in entrada:
        partes = entrada.split("-")
        if entrada.startswith("-"):
            desde = 1  # Si el rango empieza con '-', se toma 1 como límite inferior
            hasta = int(partes[1])
        elif entrada.endswith("-"):
            desde = int(partes[0])
            hasta = 60  # Si el rango termina con '-', se toma 60 como límite superior
        else:
            desde, hasta = map(int, partes)  # Caso estándar con ambos límites
    else:
        desde = hasta = int(entrada)  # Si solo se da un número, calcula solo su factorial
    
    # Verifica que los valores sean correctos
    if desde > hasta:
        print("El primer número debe ser menor o igual al segundo.")
    else:
        calcular_factoriales(desde, hasta)
except ValueError:
    print("Formato inválido. Ingrese un número o un rango en el formato correcto (ej. 4-8, -10, 5- o -60).")