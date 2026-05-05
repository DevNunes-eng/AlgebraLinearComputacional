import numpy as np
import time
from scipy.linalg import lu_factor, lu_solve

def biblioteca_gauss(A, b):
    """
    O NumPy não tem uma 'Eliminação de Gauss' pura exposta (ele usa LAPACK/LU).
    Simulamos o tempo da solução direta padrão de alto nível.
    """
    A_np = np.array(A, dtype=float)
    b_np = np.array(b, dtype=float)
    
    inicio = time.time()
    x = np.linalg.solve(A_np, b_np)
    fim = time.time()
    
    return x.tolist(), fim - inicio

def biblioteca_lu(A, b):
    """Usa a fatoração LU otimizada do SciPy (LAPACK)."""
    A_np = np.array(A, dtype=float)
    b_np = np.array(b, dtype=float)
    
    inicio = time.time()
    lu, piv = lu_factor(A_np)
    x = lu_solve((lu, piv), b_np)
    fim = time.time()
    
    return x.tolist(), fim - inicio

def biblioteca_jacobi(A, b, tol, max_iter):
    """Versão vetorizada do Método de Jacobi usando NumPy."""
    A_np = np.array(A, dtype=float)
    b_np = np.array(b, dtype=float)
    x = np.zeros_like(b_np)
    D = np.diag(A_np)
    R = A_np - np.diagflat(D)
    
    inicio = time.time()
    for i in range(max_iter):
        x_novo = (b_np - np.dot(R, x)) / D
        if np.linalg.norm(x_novo - x, ord=np.inf) < tol:
            x = x_novo
            break
        x = x_novo
    fim = time.time()
    
    return x.tolist(), fim - inicio

def biblioteca_gauss_seidel(A, b, tol, max_iter):
    """Versão otimizada de Gauss-Seidel usando estruturas triangulares do NumPy."""
    A_np = np.array(A, dtype=float)
    b_np = np.array(b, dtype=float)
    x = np.zeros_like(b_np)
    
    # L e U para Gauss-Seidel: A = L + U[cite: 2]
    L = np.tril(A_np)
    U = A_np - L
    
    inicio = time.time()
    for i in range(max_iter):
        # Resolve o sistema triangular L * x_novo = b - U * x_antigo
        x_novo = np.linalg.solve(L, b_np - np.dot(U, x))
        if np.linalg.norm(x_novo - x, ord=np.inf) < tol:
            x = x_novo
            break
        x = x_novo
    fim = time.time()
    
    return x.tolist(), fim - inicio