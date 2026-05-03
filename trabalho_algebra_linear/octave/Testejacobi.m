A = [10 2 1; 1 5 1; 2 3 10];
b = [2; 3; 10];
tol = 1e-10;
x0 = [0; 0; 0];

sol = solveJacobi(A, b, x0, tol);
disp('Solução:');
disp(sol);

