## -*- Mode: octave -*-
## Measuring online prediction accuracy of an adaptive decision rule.
## At each timestep t, the decision rule makes some prediction $C_t$.
## We check whether this prediction is inline with the data $X_t$.
## Then the decision rule is allowed to adapt. In this way, we never evaluate the prediction rule on already seen data.
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
