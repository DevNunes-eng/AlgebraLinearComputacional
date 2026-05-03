A = [10 2 1; 2 20 -2; -2 3 10];
b = [9; -44; 22];
tol = 1e-4;
x0 = [0; 0; 0];

sol = solveSeidel(A, b, x0, tol);
disp('Solução:');
disp(sol);
