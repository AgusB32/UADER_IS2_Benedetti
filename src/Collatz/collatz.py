def calcular_collatz(n):
    """Calcula la secuencia de Collatz para un número dado y devuelve el número de iteraciones."""
    iteraciones = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

def calcular_collatz_rango(inicio, fin):
    """Calcula las iteraciones de Collatz para un rango de números."""
    resultados = {}
    for num in range(inicio, fin + 1):
        iteraciones = calcular_collatz(num)
        resultados[num] = iteraciones
    return resultados