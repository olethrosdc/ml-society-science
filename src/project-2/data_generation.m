## -*- Mode: octave -*-

printf("Generating data\n");

function [X, Z] = GenerateData(n_data)
  X = zeros(10, n_data);
  Z = zeros(n_data, 1);
  for t=1:n_data
	X(1, t) = (rand < 0.5);
	X(3, t) = (rand<0.3);
	X(4, t) = (rand<0.4);
	X(5, t) = (rand<0.5);
	X(6, t) = (rand<0.6);
	X(7, t) = (rand<0.4);
	X(2, t) = (rand < 0.2 + 0.05 * X(3, t) + 0.1 * X(1, t));
	Z(t) = (rand - 0.1 * X(4, t) + 0.1 * X(5, t) - 0.1 * X(6, t));
	X(8, t) = (rand*0.5 + 0.5*Z(t)<0.5);
	if (Z > 0)
	  X(9, t) = (rand < 0.5 * X(4, t) - 0.1 * X(5, t) + 0.6 * X(6, t));
	  X(10, t) = (rand < X(2, t)*X(4, t) + X(3, t));
	else
	  X(9, t) = (rand < 0.4 * X(4, t) + 0.5 * X(6, t));
	  X(10, t) = (rand < 0.2 * X(2, t)*X(4, t) + 0.2 * X(5, t) - 0.1 * X(10,t));
	end
  end
  X = X';
end
smoker = 1

[X, Z] = GenerateData(10000);
ceil(100*[mean(X(Z<0, :)); mean(X(Z>0, :))])
 c=3; ceil(100*[mean(X(X(:,c)==0, :)); mean(X(X(:,c)!=0, :))])
 c=4; ceil(100*[mean(X(X(:,c)==0, :)); mean(X(X(:,c)!=0, :))])
 c=5; ceil(100*[mean(X(X(:,c)==0, :)); mean(X(X(:,c)!=0, :))])
