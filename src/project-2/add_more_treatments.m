load ("generating_matrices.mat");
X = load ("data/medical/historical_X.dat");
A = load ("data/medical/historical_A.dat");
Y = load ("data/medical/historical_Y.dat");

I_pos = X(:,129)==1 | X(:,130)==1;
X_pos = (X(I_pos, :));
I_neg = X(:,129)==0 & X(:,130)==0;
X_neg = (X(I_neg, :));

diff = mean(X_pos - mean(X_neg));

V_average = diff;

V = [V; V_average];
V_eye = eye(130) + repmat(V(1,:), 130,1);
for k =3:128
  V = [V; V_eye(k,:)];
  V(k,k) *= randn;
end

printf("Average treatment effect\n")
effect = mean(V * X_pos', 2);
plot(effect)

best_effect = zeros(rows(X_pos), 1);
for t=1:rows(X_pos)
  best_effect(t)= max(V * X(1, :)');
end

printf("- Best uniform treatment: %f\n- Best custom treatment: %f\n",
	   max(effect),
	   mean(best_effect))

save("-mat", "big_generating_matrices.mat", "V", "W")
