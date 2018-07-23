%% -*- Mode: octave -*-

%% Let us consider this amount of data
max_data=1000;
%% Let us run our test a few times
n_trials = 1000;

%% Get samples from two Bernoulli distributions
X = rand(max_data,n_trials)<=0.5;
Y = rand(max_data,n_trials)<=0.45;

%% Set the rejection rate
delta = 0.05;

%% test if the outcome is random
for t=1:max_data
  threshold(t) = binoinv(delta, t, 0.5);
end

figure(1)
plot(threshold ./ [1:max_data])
title("The rejection threshold as data increases");
pause

for t=1:max_data
  reject_x (t) = mean(sum(X(1:t,:)) < threshold(t));
  reject_y (t) = mean(sum(Y(1:t,:)) < threshold(t));
end
figure(2)
plot(reject_x, ';null-distributed;', reject_y, ';other distribution;')
title("How often we reject the null hypothesis");


%% However as you get more and more data, you should get more and more sure of the fact that the hypothesis is true.
function posterior = GetPosteriorHypothesis(X)
  n_trials = columns(X);
  max_data = rows(X);
for k=1:n_trials
  alpha = 1;
  beta = 1;
  log_p_marginal = 0;
  log_p_null = 0;
  for t=1:max_data
  x = X(t, k);
  p_x = (x * alpha + (1 - x)*beta) / (alpha + beta);
  alpha += x;
  beta += (1 - x);
  log_p_marginal += log(p_x);
  log_p_null += log(1/2);
  posterior(t,k) = exp(log_p_null - logAdd(log_p_marginal, log_p_null));
  end
endfor
endfunction
posterior_x = GetPosteriorHypothesis(X);
posterior_y = GetPosteriorHypothesis(Y);
figure(3);
plot(mean(posterior_x, 2), ';null-distributed;', mean(posterior_y, 2), ';other-distributed;')
legend("Posterior probability of null hypothesis");


