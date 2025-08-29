# -*- coding: utf-8 -*-
"""
Copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados.

Este programa determina los números primos dentro de un rango dado
utilizando un enfoque orientado a objetos para mayor claridad, robustez
y mantenibilidad.

Autor: Equipo IS2 - UADER FCyT
"""

import sys
import os

MAX_RANGO = 65535

class ClassPrimes:
    """Clase que encapsula la lógica para determinar si un número es primo."""

    def compute(self, n):
        """Devuelve True si n es primo, False en caso contrario."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


class PrimeApp:
    """Clase principal que gestiona la ejecución del programa."""

    def __init__(self):
        self.prime_checker = ClassPrimes()

    def limpiar_pantalla(self):
        """Limpia la pantalla en forma multiplataforma."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def validar_argumentos(self, args):
        """Valida que los argumentos de línea de comando sean enteros correctos y estén dentro del rango permitido."""
        if len(args) != 3:
            raise ValueError("Debe proporcionar exactamente dos argumentos: inicio y fin del rango.")

        try:
            inf = int(args[1])
            sup = int(args[2])
        except ValueError:
            raise ValueError("Ambos argumentos deben ser números enteros válidos.")

        if inf > sup:
            raise ValueError("El límite inferior no puede ser mayor que el superior.")
        if sup > MAX_RANGO:
            raise ValueError(f"El límite superior no puede exceder {MAX_RANGO}.")
        if inf < 0:
            raise ValueError("El límite inferior no puede ser negativo.")

        return inf, sup

    def obtener_primos_en_rango(self, inf, sup):
        """Devuelve una lista de números primos entre inf y sup (inclusive)."""
        return [n for n in range(inf, sup + 1) if self.prime_checker.compute(n)]

    def run(self, args):
        """Ejecuta la aplicación principal."""
        try:
            inf, sup = self.validar_argumentos(args)
            self.limpiar_pantalla()
            print(f"Números primos entre {inf} y {sup} son:\n")
            primos = self.obtener_primos_en_rango(inf, sup)
            print(" ".join(map(str, primos)))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    app = PrimeApp()
    app.run(sys.argv)
