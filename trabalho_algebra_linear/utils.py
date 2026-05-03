# utils.py
# Funções de apoio para operações com matrizes e vetores.

import math


def copiar_vetor(vetor):
    return [valor for valor in vetor]


def copiar_matriz(matriz):
    return [[valor for valor in linha] for linha in matriz]


def produto_matriz_vetor(matriz, vetor):
    n = len(matriz)
    resultado = [0.0] * n
    for i in range(n):
        soma = 0.0
        for j in range(len(vetor)):
            soma += matriz[i][j] * vetor[j]
        resultado[i] = soma
    return resultado


def residual(matriz, x, b):
    Ax = produto_matriz_vetor(matriz, x)
    return [b[i] - Ax[i] for i in range(len(b))]


def norma_vetor(vetor):
    soma = 0.0
    for valor in vetor:
        soma += valor * valor
    return math.sqrt(soma)


def erro_relativo(matriz, x, b):
    r = residual(matriz, x, b)
    norma_b = norma_vetor(b)
    norma_r = norma_vetor(r)
    if norma_b == 0.0:
        return norma_r
    return norma_r / norma_b


def verificar_solucao(matriz, x, b, tol=1e-12):
    r = residual(matriz, x, b)
    erro = norma_vetor(r)
    if erro < tol:
        return True, erro
    return False, erro
