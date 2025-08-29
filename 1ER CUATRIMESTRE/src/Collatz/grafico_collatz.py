import matplotlib.pyplot as plt

def graficar_collatz(resultados):
    """Genera un gráfico de los resultados de Collatz."""
    numeros = list(resultados.keys())
    iteraciones = list(resultados.values())
    
    plt.figure(figsize=(12, 6))
    plt.scatter(iteraciones, numeros, s=1, alpha=0.5)
    plt.title('Conjetura de Collatz (1-10,000)')
    plt.xlabel('Número de iteraciones para converger')
    plt.ylabel('Número inicial (n)')
    plt.grid(True, alpha=0.3)
    
    # Guardar el gráfico
    plt.savefig('collatz_plot.png')
    plt.close()
    print("Gráfico generado y guardado como 'collatz_plot.png'")