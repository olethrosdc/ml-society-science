%% -*- Mode: octave -*-

X=[0:300]/100;
hold off;
mean_Y = 0 * X;
n_functions = 100;
for i=1:n_functions
    alpha = rand;
    beta = rand;
    Y = sin(alpha * X + beta);
    plot(X, Y, '--');
    mean_Y += Y;
    hold on
    sleep(0.01)
end
mean_Y /= n_functions;
plot(X, mean_Y, "b;function;", "linewidth", 3)
