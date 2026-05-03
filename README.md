# Trabalho de Álgebra Linear Computacional

Este repositório organiza o projeto por linguagem e responsabilidade.

## Estrutura do repositório

- `trabalho_algebra_linear/python/`
  - `main.py` - ponto de entrada em Python
  - `dados.py` - matriz A, vetores b, tolerância e iterações
  - `utils.py` - funções comuns (norma, resíduo, erro relativo, verificação)
  - `gauss.py` - eliminação gaussiana com substituição regressiva
  - `lu.py` - fatoração LU e resolução LU
  - `jacobi.py` - método de Jacobi
  - `gauss_seidel.py` - método de Gauss-Seidel
  - `grafico.py` - gráfico de convergência dos métodos iterativos

- `trabalho_algebra_linear/octave/`
  - arquivos Octave/MATLAB dos métodos Jacobi e Gauss-Seidel

- `trabalho_algebra_linear/legacy/`
  - scripts antigos de experimentação mantidos para referência

## Como usar

Entre na pasta `trabalho_algebra_linear/python/` e execute:

```bash
python3 main.py
```

O código roda sem NumPy ou SciPy e usa apenas bibliotecas básicas de Python.

## Observações

- A estrutura agora separa por linguagem (`python/` e `octave/`).
- Dentro de cada linguagem, os arquivos estão organizados por responsabilidade.
- `legacy/` preserva códigos antigos que podem ser mantidos como referência.
