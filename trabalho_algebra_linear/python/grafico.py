# grafico.py
# Geração do gráfico de convergência dos métodos iterativos.

import matplotlib.pyplot as plt


def plot_convergencia(it_jacobi, log_jacobi, it_gs, log_gs):
    plt.figure(figsize=(10, 6))
    plt.plot(it_jacobi, log_jacobi, marker='o', color='blue', linestyle='-', label='Jacobi')
    plt.plot(it_gs, log_gs, marker='s', color='red', linestyle='--', label='Gauss-Seidel')
    plt.title('Convergência dos Métodos Iterativos')
    plt.xlabel('Número de Iterações')
    plt.ylabel('log10(Erro Relativo)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
