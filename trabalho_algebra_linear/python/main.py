# main.py
# Execução dos métodos diretos e iterativos para o trabalho de Álgebra Linear Computacional.

import time

from dados import A, vetores_b, tolerancia, max_iteracoes
from utils import erro_relativo, verificar_solucao, produto_matriz_vetor
from gauss import eliminacao_gaussiana
from lu import solve as resolver_lu
from jacobi import jacobi
from gauss_seidel import gauss_seidel
from grafico import plot_convergencia


def imprimir_resultados(metodo, x, A, b, tempo_execucao):
    print(f"Resultado do método: {metodo}")
    print(f"Solução aproximada: {[round(valor, 10) for valor in x]}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
    erro = erro_relativo(A, x, b)
    print(f"Erro relativo final: {erro:.10e}")
    valido, norma_residuo = verificar_solucao(A, x, b)
    print(f"Verificação da solução: {'OK' if valido else 'Falha'}")
    print(f"Norma do resíduo: {norma_residuo:.10e}")
    print("Resultado de A*x:", [round(valor, 10) for valor in produto_matriz_vetor(A, x)])
    print("Vetor b original:", [round(valor, 10) for valor in b])
    print("-" * 60)


def executar_metodos_diretos(A, b):
    print("\nMétodos diretos para vetor b =", b)
    try:
        inicio = time.time()
        x_gauss = eliminacao_gaussiana(A, b)
        fim = time.time()
        imprimir_resultados('Eliminação de Gauss', x_gauss, A, b, fim - inicio)
    except Exception as erro:
        print("Erro na eliminação de Gauss:", erro)

    try:
        inicio = time.time()
        x_lu = resolver_lu(A, b)
        fim = time.time()
        imprimir_resultados('Fatoração LU', x_lu, A, b, fim - inicio)
    except Exception as erro:
        print("Erro na fatoração LU:", erro)


def executar_metodos_iterativos(A, b, tol, max_iter):
    print("\nMétodos iterativos para vetor b =", b)
    print("Jacobi:")
    inicio = time.time()
    x_jacobi, iter_jacobi, log_jacobi = jacobi(A, b, tol, max_iter)
    fim = time.time()
    imprimir_resultados('Jacobi', x_jacobi, A, b, fim - inicio)

    print("Gauss-Seidel:")
    inicio = time.time()
    x_gs, iter_gs, log_gs = gauss_seidel(A, b, tol, max_iter)
    fim = time.time()
    imprimir_resultados('Gauss-Seidel', x_gs, A, b, fim - inicio)

    return iter_jacobi, log_jacobi, iter_gs, log_gs


def main():
    print("Trabalho de Álgebra Linear Computacional")
    print("Matriz A:")
    for linha in A:
        print(linha)
    print("-" * 60)

    for indice, b in enumerate(vetores_b, start=1):
        print(f"\n===== Vetor b #{indice} =====")
        executar_metodos_diretos(A, b)
        iter_jacobi, log_jacobi, iter_gs, log_gs = executar_metodos_iterativos(
            A, b, tolerancia, max_iteracoes
        )
        if iter_jacobi and iter_gs:
            plot_convergencia(iter_jacobi, log_jacobi, iter_gs, log_gs)


if __name__ == '__main__':
    main()
