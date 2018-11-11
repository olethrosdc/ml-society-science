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
V_eye = eye(130);
for k =3:128
  V = [V; V_eye(k,:)];
end

printf("Average treatment effect\n")
mean(V * X_pos', 2)
