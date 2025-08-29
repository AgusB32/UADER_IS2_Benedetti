from Collatz.collatz import calcular_collatz_rango
from Collatz.grafico_collatz import graficar_collatz

def main():
    print("Calculando secuencias de Collatz para números del 1 al 10,000...")
    resultados = calcular_collatz_rango(1, 10000)
    graficar_collatz(resultados)

if __name__ == "__main__":
    main()  