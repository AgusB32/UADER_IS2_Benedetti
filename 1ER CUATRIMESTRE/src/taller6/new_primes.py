# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: old_primes.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 18:42:35 UTC (1746556955)

import os
import sys

if len(sys.argv) != 3:
    print("Error: Debe ingresar dos números como argumentos (límite inferior y límite superior).")
    print("Uso: python script.py <inferior> <superior>")
    exit()

try:
    lower = int(sys.argv[1])
    upper = int(sys.argv[2])
except ValueError:
    print("Error: Ambos argumentos deben ser números enteros.")
    exit()

os.system('clear')

if lower > upper:
    print("Por favor ingrese nuevamente dos valores válidos: el primero menor o igual que el segundo.")
    exit()

print('Números primos entre %d y %d son:\n' % (lower, upper))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print('%d ' % num)
