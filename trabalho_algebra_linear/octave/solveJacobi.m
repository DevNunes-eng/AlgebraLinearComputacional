function [x] = solveJacobi(A, b, x, tol)
  n = size(A, 1);
  x0 = x;
  iter = 1;
  nmax = 10000;

  while iter <= nmax
    for i = 1:n

      x(i) = (b(i) - A(i, [1:i-1, i+1:n]) * x0([1:i-1, i+1:n])) / A(i, i);
    endfor


    if norm(x - x0, inf) < tol
      disp('Número de iterações:');
      disp(iter);
      return;
    endif


    x0 = x;
    iter = iter + 1;
  endwhile


  error('Número máximo de iterações excedido');
endfunction
