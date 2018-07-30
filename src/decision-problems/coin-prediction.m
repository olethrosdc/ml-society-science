## -*- Mode: octave -*-

T = 100;
alpha = 1;
beta = 1;
p = 0.6;

C = rand(T,1)<=p;
for t=1:T
  if (alpha > beta)
	prediction = 1;
  else
	prediction = 0;
  end
  X(t) = (prediction == C(t));
  alpha += C(t);
  beta += (1 - C(t));
end
mean(X)
