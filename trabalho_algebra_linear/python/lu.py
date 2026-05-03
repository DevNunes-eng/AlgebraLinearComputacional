# lu.py
# Implementação de fatoração LU e resolução de sistemas usando LU.

from utils import copiar_matriz, copiar_vetor


def fatoracao_lu(A):
    A = copiar_matriz(A)
    n = len(A)
    L = [[0.0 if i != j else 1.0 for j in range(n)] for i in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            soma = 0.0
            for k in range(i):
                soma += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - soma

        if U[i][i] == 0.0:
            raise ValueError("Pivô zero encontrado na fatoração LU.")

        for j in range(i + 1, n):
            soma = 0.0
            for k in range(i):
                soma += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - soma) / U[i][i]

    return L, U


def resolver_lu(L, U, b):
    n = len(L)
    y = [0.0] * n

    # Substituição progressiva Ly = b
    for i in range(n):
        soma = 0.0
        for j in range(i):
            soma += L[i][j] * y[j]
        y[i] = b[i] - soma

    # Substituição regressiva Ux = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = 0.0
        for j in range(i + 1, n):
            soma += U[i][j] * x[j]
        if U[i][i] == 0.0:
            raise ValueError("Pivô zero encontrado na resolução LU.")
        x[i] = (y[i] - soma) / U[i][i]

    return x


def solve(A, b):
    L, U = fatoracao_lu(A)
    return resolver_lu(L, U, b)
