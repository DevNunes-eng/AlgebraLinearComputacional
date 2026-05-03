import math

def jacobi_igual_octave(A, b, tol, max_iter):
    n = len(A)
    x = [0.0] * n 
    
    print(f"{'Iter':<5} | {'Erro (Norma Inf)':<20}")
    print("-" * 30)

    for k in range(1, max_iter + 1):
        x_novo = [0.0] * n
        
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if i != j:
                    soma += A[i][j] * x[j]
            x_novo[i] = (b[i] - soma) / A[i][i]
        
        maior_diff = 0.0
        for i in range(n):
            diff = abs(x_novo[i] - x[i])
            if diff > maior_diff:
                maior_diff = diff
        
        print(f"{k:<5} | {maior_diff:<20.10e}")

        
        if maior_diff < tol:
            print("-" * 30)
            print(f"Convergência em {k} iterações.")
            return x_novo
        
    
        x = x_novo[:]

    return x


A = [[10, 2, 1], [1, 5, 1], [2, 3, 10]]
b = [2, 3, 10]
tol = 1e-10

solucao = jacobi_igual_octave(A, b, tol, 100)
print("\nSolução Final:", solucao)