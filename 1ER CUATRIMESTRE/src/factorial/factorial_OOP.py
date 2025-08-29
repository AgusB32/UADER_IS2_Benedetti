import sys

class Factorial:
    def __init__(self):
        pass  # No se requiere inicialización específica

    def calcular(self, num):
        """Calcula el factorial de un número."""
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

    def run(self, min_val, max_val):
        """Calcula los factoriales en el rango especificado."""
        for num in range(min_val, max_val + 1):
            print(f"Factorial {num}! es {self.calcular(num)}")

# Verifica si se pasó un argumento en la línea de comandos, de lo contrario, solicita entrada al usuario
if len(sys.argv) < 2:
    entrada = input("Ingrese un rango (ej. 4-8, -10, 5- o -60): ")
else:
    entrada = sys.argv[1]

try:
    if "-" in entrada:
        partes = entrada.split("-")
        if entrada.startswith("-"):
            desde = 1
            hasta = int(partes[1])
        elif entrada.endswith("-"):
            desde = int(partes[0])
            hasta = 60
        else:
            desde, hasta = map(int, partes)
    else:
        desde = hasta = int(entrada)
    
    if desde > hasta:
        print("El primer número debe ser menor o igual al segundo.")
    else:
        factorial_obj = Factorial()
        factorial_obj.run(desde, hasta)
except ValueError:
    print("Formato inválido. Ingrese un número o un rango en el formato correcto (ej. 4-8, -10, 5- o -60).")
