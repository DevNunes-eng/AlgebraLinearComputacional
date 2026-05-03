function [x] = solveSeidel(A, b, x, tol)
  n = size(A, 1);
  iter = 0;
  nmax = 10000;
  x0 = x;

  while iter <= nmax
    x_old = x;

    for i = 1:n
      % Soma dos termos anteriores e posteriores
      soma = A(i, 1:i-1) * x(1:i-1) + A(i, i+1:n) * x_old(i+1:n);
      x(i) = (b(i) - soma) / A(i, i);
    endfor

    % Critério de parada usando norma infinita
    if norm(x - x_old, inf) < tol
      disp('Número de iterações:');
      disp(iter);
      return;
    endif

    iter = iter + 1;
  endwhile

  error('Número máximo de iterações excedido');
endfunction

