## -*- Mode: octave -*-

printf("Generating data\n");

function [X, Z, A, Y] = GenerateData(n_data, W, V)
  X = zeros(10, n_data);
  Z = zeros(n_data, 1);
  A = zeros(n_data, 1);
  Y = zeros(n_data, 1);
  for t=1:n_data
	X(1:128, t) = (randn(1,rows(W)) * W < 0);
	X(1, t) = (rand < 0.5);
	X(2, t) = (rand < 0.2 + 0.05 * X(3, t) + 0.1 * X(1, t));
	Z(t) = (rand - 0.2 * X(4, t) + 0.2 * X(5, t) - 0.2 * X(6, t));
	X(128, t) = ((rand*0.5 + 0.5*Z(t))<0.5);
	if (Z > 0)
	  X(129, t) = (rand < 0.5 * X(4, t) - 0.1 * X(5, t) + 0.6 * X(6, t));
	  X(130, t) = (rand < X(2, t)*X(4, t) + X(3, t));
	else
	  X(129, t) = (rand < 0.4 * X(4, t) + 0.5 * X(6, t));
	  X(130, t) = (rand < 0.2 * X(2, t)*X(4, t) + 0.2 * X(5, t) - 0.1 * X(10,t));
	end
	A(t) = (rand < X(129, t) * 0.4  + X(130, t) * 0.5);
	#Y(t) = rand < sigmoid(V(A(t)+1, :) * X(:,t));
	Y(t) = V(A(t)+1, :) * X(:,t) > 0;
  end
  X = X';

end
smoker = 1

load ("generating_matrices.data")

[X, Z, A, Y] = GenerateData(10000, W, V);
ceil(100*[mean(X(Z<0, :)); mean(X(Z>0, :))])
c=3; ceil(100*[mean(X(X(:,c)==0, :)); mean(X(X(:,c)!=0, :))])
c=4; ceil(100*[mean(X(X(:,c)==0, :)); mean(X(X(:,c)!=0, :))])
c=5; ceil(100*[mean(X(X(:,c)==0, :)); mean(X(X(:,c)!=0, :))])
