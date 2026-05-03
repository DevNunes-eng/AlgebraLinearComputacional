# jacobi.py
# Implementação do método iterativo de Jacobi.

from utils import copiar_vetor, erro_relativo
import math
import time


def jacobi(A, b, tol, max_iter, x0=None):
    n = len(A)
    x = copiar_vetor(x0) if x0 is not None else [0.0] * n
    historico_iteracoes = []
    historico_log_rel = []

    print(f"{'Iteração':<10} | {'Erro Relativo':<20}")
    print("-" * 40)

    for k in range(1, max_iter + 1):
        x_novo = [0.0] * n
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * x[j]
            x_novo[i] = (b[i] - soma) / A[i][i]

        erro = erro_relativo(A, x_novo, b)
        log_rel = math.log10(erro) if erro > 0 else -math.inf
        historico_iteracoes.append(k)
        historico_log_rel.append(log_rel)

        print(f"{k:<10} | {erro:<20.10e}")

        x = x_novo
        if erro < tol:
            print("-" * 40)
            print(f"Convergência atingida em {k} iterações.\n")
            break
    else:
        print("-" * 40)
        print("Aviso: número máximo de iterações atingido.\n")

    return x, historico_iteracoes, historico_log_rel
