# dados.py
# Definição da matriz A, dos vetores b, da tolerância e do número máximo de iterações.

A = [
    [10.0, 2.0, 1.0],
    [1.0, 5.0, 1.0],
    [2.0, 3.0, 10.0]
]

vetores_b = [
    [7.0, -8.0, 6.0],
    [2.0, 3.0, 10.0]
]

# Tolerância para os métodos iterativos
tolerancia = 1e-10

# Número máximo de iterações para Jacobi e Gauss-Seidel
max_iteracoes = 100

# Caso queira adicionar mais vetores b, basta incluir novos elementos em vetores_b.
