import time
import math
import matplotlib.pyplot as plt

def jacobi(A, b, tol, max_iter):
    n = len(A)
    # Chute inicial zero
    x = [0.0] * n
    x_new = [0.0] * n

    historico_log_res = []
    iteracoes = []

    start_time = time.time()

    print(f"{'Iteração':<10} | {'Norma do Resíduo':<20}")
    print("-" * 35)

    for k in range(1, max_iter + 1):
        # --- PASSO 1: Cálculo do novo x (Jacobi) ---
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if i != j:
                    soma += A[i][j] * x[j]
            x_new[i] = (b[i] - soma) / A[i][i]

        # --- PASSO 2: Cálculo da Norma do Resíduo Verdadeiro (r = b - Ax) ---
        # Calculando o vetor resíduo r_vetor = b - (A * x_new)
        soma_quadrados_r = 0.0
        for i in range(n):
            ax_i = 0.0
            for j in range(n):
                ax_i += A[i][j] * x_new[j]
            
            resíduo_i = b[i] - ax_i
            soma_quadrados_r += resíduo_i**2
        
        norma_r = math.sqrt(soma_quadrados_r)

        # --- PASSO 3: Atualização e Logs ---
        for i in range(n):
            x[i] = x_new[i]

        # Evita erro de log(0) caso o resíduo seja exatamente zero
        log_res = math.log10(norma_r) if norma_r > 0 else -16
        historico_log_res.append(log_res)
        iteracoes.append(k)

        print(f"{k:<10} | {norma_r:<20.10e}")

        # Critério de parada baseado na norma do resíduo
        if norma_r < tol:
            print("-" * 35)
            print(f"Convergência atingida em {k} iterações.")
            break
    else:
        print("-" * 35)
        print("Aviso: Número máximo de iterações atingido.")

    end_time = time.time()
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

    return x, iteracoes, historico_log_res

# --- Exemplo de teste (Matriz de Poisson 1D / SPD) ---
A_exemplo = [
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4]
]
b_exemplo = [7, -8, 6]

# Execução
solucao, iters, logs = jacobi(A_exemplo, b_exemplo, tol=1e-10, max_iter=100)

print("\nSolução Final:", solucao)

# --- Gerar o Gráfico (Exigência do item 2) ---
plt.figure(figsize=(8, 5))
plt.plot(iters, logs, marker='o', color='red', linestyle='-')
plt.title('Histórico de Convergência - log10(Norma do Resíduo)')
plt.xlabel('Número de Iterações')
plt.ylabel('log10(||b - Ax||)')
plt.grid(True)
plt.show()