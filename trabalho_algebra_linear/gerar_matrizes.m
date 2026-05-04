clear variables
close all
clc

% ==========================================================
% GERADOR DE MATRIZES PARA BENCHMARK
% Álgebra Linear Computacional
% ==========================================================

rng(1); % fixa a semente para tornar os testes reproduzíveis

% Tamanhos escolhidos
n1 = 10;   % Teste 1: SPD diagonalmente dominante
n2 = 50;   % Teste 2: aleatória geral não singular
n3 = 50;   % Teste 3: Poisson 1D

% ==========================================================
% TESTE 1: Matriz SPD diagonalmente dominante
% ==========================================================

M = rand(n1);
A1 = M' * M;              % torna a matriz simétrica positiva semidefinida
delta = norm(A1);

for i = 1:n1
    soma = sum(abs(A1(i,:))) - abs(A1(i,i));
    A1(i,i) = soma + delta; % força dominância diagonal
end

x1_exato = ones(n1,1);
b1 = A1 * x1_exato;

writematrix(A1, 'A1_SPD_diagonal_dominante.csv');
writematrix(b1, 'b1_SPD_diagonal_dominante.csv');
writematrix(x1_exato, 'x1_exato_SPD_diagonal_dominante.csv');

% ==========================================================
% TESTE 2: Matriz aleatória geral não singular
% ==========================================================

A2 = rand(n2);

while rcond(A2) < 1e-12
    A2 = rand(n2);
end

x2_exato = ones(n2,1);
b2 = A2 * x2_exato;

writematrix(A2, 'A2_aleatoria_geral.csv');
writematrix(b2, 'b2_aleatoria_geral.csv');
writematrix(x2_exato, 'x2_exato_aleatoria_geral.csv');

% ==========================================================
% TESTE 3: Matriz de Poisson 1D
% ==========================================================

h = 1/(n3+1);
A3 = zeros(n3,n3);

for i = 1:n3
    A3(i,i) = 2/(h^2);

    if i > 1
        A3(i,i-1) = -1/(h^2);
    end

    if i < n3
        A3(i,i+1) = -1/(h^2);
    end
end

x3_exato = ones(n3,1);
b3 = A3 * x3_exato;

writematrix(A3, 'A3_poisson_1D.csv');
writematrix(b3, 'b3_poisson_1D.csv');
writematrix(x3_exato, 'x3_exato_poisson_1D.csv');

disp('Matrizes geradas com sucesso.')
disp('Arquivos CSV salvos na mesma pasta do script.')