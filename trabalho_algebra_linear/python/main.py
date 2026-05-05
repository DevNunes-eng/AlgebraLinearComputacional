import time
import sys
from utils import verificar_solucao, erro_relativo
from grafico import plot_convergencia

# Importações dos métodos manuais
from gauss import eliminacao_gaussiana
from lu import solve as resolver_lu
from jacobi import jacobi
from gauss_seidel import gauss_seidel

# Importações dos métodos com biblioteca
from implementacoes_biblioteca import (
    biblioteca_gauss, biblioteca_lu, 
    biblioteca_jacobi, biblioteca_gauss_seidel
)

def carregar_contexto(opcao):
    if opcao == '1':
        import dados_teste1_spd as d
    elif opcao == '2':
        import dados_teste2_aleatoria as d
    elif opcao == '3':
        import dados_teste3_poisson as d
    else:
        import nos6 as d
    return d.A, d.vetores_b[0], d.tolerancia, d.max_iteracoes, getattr(d, 'n', len(d.A))

def imprimir_resumo(metodo, x, A, b, tempo, tol_verif):
    valido, residuo = verificar_solucao(A, x, b, tol=tol_verif)
    status = "OK" if valido else "Falha"
    # Para salvar a solução completa em um arquivo e conferir no bloco de notas
    with open("solucao_final.txt", "w") as f:
        for valor in x:
            f.write(f"{valor}\n")
    print(f"[{metodo}] Tempo: {tempo:.6f}s | Resíduo: {residuo:.2e} | Status: {status}")

def menu_principal():
    print("\n" + "="*50)
    print("SISTEMA DE ANÁLISE DE ÁLGEBRA LINEAR - UFRJ")
    print("="*50)
    
    print("\nPARTE 1: SELECIONE A MATRIZ")
    print("1 - SPD (Simétrica Positiva Definida)")
    print("2 - Aleatória (Teste de Estabilidade)")
    print("3 - Poisson (Sistemas Esparsos)")
    print("4 - nos6 (Matrix Market - Ordem 675)")
    mat_opt = input("Escolha: ")

    A, b, tol, m_iter, n = carregar_contexto(mat_opt)
    # Ajuste automático da tolerância de verificação conforme a matriz
    t_verif = 1e-7 if mat_opt == '4' else 1e-12

    print("\nPARTE 2: SELECIONE A EXECUÇÃO")
    print("1 - Todos os métodos (SEM biblioteca)")
    print("2 - Todos os métodos (COM biblioteca)")
    print("3 - Gerar Tabela Comparativa (Manual vs Biblioteca)")
    print("4 - Executar método individualmente")
    exe_opt = input("Escolha: ")

    if exe_opt == '1':
        executar_todos(A, b, tol, m_iter, t_verif, modo='manual')
    elif exe_opt == '2':
        executar_todos(A, b, tol, m_iter, t_verif, modo='biblioteca')
    elif exe_opt == '3':
        executar_comparacao_completa(A, b, tol, m_iter, t_verif)
    elif exe_opt == '4':
        executar_individual(A, b, tol, m_iter, t_verif)

def executar_todos(A, b, tol, m_iter, t_verif, modo):
    print(f"\n--- Executando todos os métodos ({modo.upper()}) ---")
    if modo == 'manual':
        s = time.time(); x = eliminacao_gaussiana(A, b); imprimir_resumo("Gauss", x, A, b, time.time()-s, t_verif)
        s = time.time(); x = resolver_lu(A, b); imprimir_resumo("LU", x, A, b, time.time()-s, t_verif)
        s = time.time(); x, it, log_j = jacobi(A, b, tol, m_iter); imprimir_resumo("Jacobi", x, A, b, time.time()-s, t_verif)
        s = time.time(); x, it_s, log_s = gauss_seidel(A, b, tol, m_iter); imprimir_resumo("G-Seidel", x, A, b, time.time()-s, t_verif)
        plot_convergencia(it, log_j, it_s, log_s)
    else:
        x, t = biblioteca_gauss(A, b); imprimir_resumo("Gauss Bib", x, A, b, t, t_verif)
        x, t = biblioteca_lu(A, b); imprimir_resumo("LU Bib", x, A, b, t, t_verif)
        x, t = biblioteca_jacobi(A, b, tol, m_iter); imprimir_resumo("Jacobi Bib", x, A, b, t, t_verif)
        x, t = biblioteca_gauss_seidel(A, b, tol, m_iter); imprimir_resumo("G-Seidel Bib", x, A, b, t, t_verif)

def executar_comparacao_completa(A, b, tol, m_iter, t_verif):
    # Dicionários para armazenar tempos e permitir o cálculo de speedup
    m_t = {}; b_t = {}
    
    # Execuções Manuais
    s = time.time(); eliminacao_gaussiana(A, b); m_t['Gauss'] = time.time()-s
    s = time.time(); resolver_lu(A, b); m_t['LU'] = time.time()-s
    s = time.time(); x_j, it_j, log_j = jacobi(A, b, tol, m_iter); m_t['Jacobi'] = time.time()-s
    s = time.time(); x_s, it_s, log_s = gauss_seidel(A, b, tol, m_iter); m_t['Gauss-Seidel'] = time.time()-s
    
    # Execuções Biblioteca
    _, b_t['Gauss'] = biblioteca_gauss(A, b)
    _, b_t['LU'] = biblioteca_lu(A, b)
    _, b_t['Jacobi'] = biblioteca_jacobi(A, b, tol, m_iter)
    _, b_t['Gauss-Seidel'] = biblioteca_gauss_seidel(A, b, tol, m_iter)
    
    print("\n" + "="*75)
    print(f"{'MÉTODO':<20} | {'MANUAL (s)':<15} | {'BIBLIOTECA (s)':<15} | {'SPEEDUP'}")
    print("-" * 75)
    for metodo in ['Gauss', 'LU', 'Jacobi', 'Gauss-Seidel']:
        speedup = m_t[metodo]/b_t[metodo] if b_t[metodo] > 0 else 0
        print(f"{metodo:<20} | {m_t[metodo]:<15.6f} | {b_t[metodo]:<15.6f} | {speedup:.2f}x")
    print("="*75)
    plot_convergencia(it_j, log_j, it_s, log_s)

def executar_individual(A, b, tol, m_iter, t_verif):
    print("\nEscolha o método: 1-Gauss, 2-LU, 3-Jacobi, 4-Gauss-Seidel")
    m_opt = input("Escolha: ")
    metodos = { '1': ('Gauss', eliminacao_gaussiana, biblioteca_gauss),
                '2': ('LU', resolver_lu, biblioteca_lu),
                '3': ('Jacobi', jacobi, biblioteca_jacobi),
                '4': ('Gauss-Seidel', gauss_seidel, biblioteca_gauss_seidel) }
    
    nome, func_m, func_b = metodos[m_opt]
    
    # Manual
    s = time.time()
    res_m = func_m(A, b) if m_opt in ['1','2'] else func_m(A, b, tol, m_iter)
    x_m = res_m[0] if m_opt in ['3','4'] else res_m
    t_m = time.time() - s
    
    # Biblioteca
    x_b, t_b = func_b(A, b) if m_opt in ['1','2'] else func_b(A, b, tol, m_iter)
    
    print(f"\n--- Comparação Individual: {nome} ---")
    imprimir_resumo(f"{nome} Manual", x_m, A, b, t_m, t_verif)
    imprimir_resumo(f"{nome} Biblioteca", x_b, A, b, t_b, t_verif)

if __name__ == "__main__":
    while True:
        menu_principal()
        if input("\nDeseja realizar outro teste? (s/n): ").lower() != 's':
            break