import time
import math
import matplotlib.pyplot as plt

def jacobi(A, b, tol, max_iter):
    n = len(A)
    # Vetor inicial x (chute inicial zero)
    x = [0.0] * n
    x_new = [0.0] * n
    
    historico_log_res = []
    iteracoes = []
    
    start_time = time.time()
    
    print(f"{'Iteração':<10} | {'Resíduo (Erro Relat.)':<20}")
    print("-" * 35)

    for k in range(1, max_iter + 1):
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if i != j:
                    soma += A[i][j] * x[j]
            
            # Cálculo do novo x_i
            x_new[i] = (b[i] - soma) / A[i][i]
        
        # Cálculo da Norma do Resíduo (Erro Relativo Euclidiano)
        norma_diff = 0.0
        norma_x_new = 0.0
        for i in range(n):
            norma_diff += (x_new[i] - x[i])**2
            norma_x_new += x_new[i]**2
            x[i] = x_new[i] # Atualiza para a próxima iteração
            
        erro_relativo = math.sqrt(norma_diff) / math.sqrt(norma_x_new)
        
        # Logs e histórico para o gráfico
        log_res = math.log10(erro_relativo)
        historico_log_res.append(log_res)
        iteracoes.append(k)
        
        print(f"{k:<10} | {erro_relativo:<20.10e}")
        
        if erro_relativo < tol:
            print("-" * 35)
            print(f"Convergência atingida em {k} iterações.")
            break
    else:
        print("-" * 35)
        print("Aviso: Número máximo de iterações atingido.")

    end_time = time.time()
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
    
    return x, iteracoes, historico_log_res

# --- Exemplo de uso (Matriz diagonal dominante) ---
A_exemplo = [
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
]
b_exemplo = [7, -8, 6]

solucao, iters, logs = jacobi(A_exemplo, b_exemplo, tol=1e-10, max_iter=100)
print("Solução Final Python:", solucao)
# Gerar o Gráfico
plt.figure(figsize=(8, 5))
plt.plot(iters, logs, marker='o', color='b', linestyle='-')
plt.title('Histórico de Convergência (Jacobi)')
plt.xlabel('Número de Iterações')
plt.ylabel('log10(Norma do Resíduo)')
plt.grid(True)
plt.show()