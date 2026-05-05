# nos6.py
import os

def carregar_matrix_market(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo {caminho_arquivo} não encontrado.")

    with open(caminho_arquivo, 'r') as f:
        # Pula comentários que começam com %
        linhas = [linha for linha in f if not linha.startswith('%')]
        
        # A primeira linha de dados contém: linhas, colunas e entradas não-nulas
        # Ex: 675 675 1965
        n_linhas, n_colunas, n_nao_nulas = map(int, linhas[0].split())
        
        # Inicializa a matriz densa com zeros
        matriz_a = [[0.0 for _ in range(n_colunas)] for _ in range(n_linhas)]
        
        # Preenche a matriz usando as coordenadas (convertendo base 1 para base 0)
        for i in range(1, len(linhas)):
            l, c, valor = linhas[i].split()
            idx_l, idx_c = int(l) - 1, int(c) - 1
            val = float(valor)
            
            matriz_a[idx_l][idx_c] = val
            # Devido à flag 'symmetric', espelhamos os valores fora da diagonal
            if idx_l != idx_c:
                matriz_a[idx_c][idx_l] = val
                
    return matriz_a, n_linhas

# Configurações do teste
caminho = "trabalho_algebra_linear\\python\\nos6.mtx.txt"
A, n = carregar_matrix_market(caminho)

# Como o arquivo .mtx não fornece o vetor b, criamos um b padrão
# Estratégia: b tal que a solução exata x seja um vetor de 1s
vetores_b = [[sum(linha) for linha in A]] # b = A * [1, 1, ..., 1]^T

tolerancia = 1e-8
max_iteracoes = 1000