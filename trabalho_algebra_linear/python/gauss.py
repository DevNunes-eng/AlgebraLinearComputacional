# gauss.py
# Implementação da eliminação de Gauss com substituição regressiva.

from utils import copiar_matriz, copiar_vetor


def substituicao_regressiva(U, y):
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if U[i][i] == 0.0:
            raise ValueError("Pivô zero encontrado na substituição regressiva.")
        soma = 0.0
        for j in range(i + 1, n):
            soma += U[i][j] * x[j]
        x[i] = (y[i] - soma) / U[i][i]
    return x


def eliminacao_gaussiana(A, b):
    A = copiar_matriz(A)
    b = copiar_vetor(b)
    n = len(A)

    for k in range(n - 1):
        # Escolha de pivô parcial para maior estabilidade
        max_linha = k
        max_valor = abs(A[k][k])
        for i in range(k + 1, n):
            if abs(A[i][k]) > max_valor:
                max_valor = abs(A[i][k])
                max_linha = i
        if max_valor == 0.0:
            raise ValueError("Matriz singular ou pivô zero encontrado.")
        if max_linha != k:
            A[k], A[max_linha] = A[max_linha], A[k]
            b[k], b[max_linha] = b[max_linha], b[k]

        for i in range(k + 1, n):
            fator = A[i][k] / A[k][k]
            A[i][k] = 0.0
            for j in range(k + 1, n):
                A[i][j] -= fator * A[k][j]
            b[i] -= fator * b[k]

    return substituicao_regressiva(A, b)
