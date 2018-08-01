%% -*- Mode: octave -*-

%% Let us consider this amount of data
max_data=1000;
%% Let us run our test a few times
n_trials = 1000;

%% Get samples from two Bernoulli distributions
X = rand(max_data,n_trials)<=0.5;
Y = rand(max_data,n_trials)<=0.55;

%% Set the rejection rate
delta = 0.05;

if (0) 
%% test if the outcome is random
for t=1:max_data
  printf("%d\n", t); fflush(stdout);
  threshold(t) = t -binoinv(delta, t, 0.5);
end

figure(1)
semilogx(threshold ./ [1:max_data])
title("The rejection threshold as data increases");
ylabel("Success rate");
xlabel("Amount of throws")
matlab2tikz("p-value-example-rejection-threshold.tikz", 'height', '\fheight', 'width', '\fwidth' );
end

for t=1:max_data
  reject_x (t) = mean(sum(X(1:t,:)) >= threshold(t));
  reject_y (t) = mean(sum(Y(1:t,:)) >= threshold(t));
end
figure(2)
plot(reject_x, ';null-distributed;', reject_y, ';other distribution;')
title("How often we reject the null hypothesis");
matlab2tikz("p-value-example-rejection.tikz",  'height', '\fheight', 'width', '\fwidth' );


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
	endfor
  endfor
endfunction
posterior_x = GetPosteriorHypothesis(X);
posterior_y = GetPosteriorHypothesis(Y);
figure(3);
plot(mean(posterior_x, 2), ';null-distributed;', mean(posterior_y, 2), ';other-distributed;')
title("Posterior probability of null hypothesis");
matlab2tikz("p-value-example-posterior.tikz",  'height', '\fheight', 'width', '\fwidth' );


figure(4);
%% ADD A PLOT FOR REJECTION

bayes_reject_x = mean(posterior_x < 0.5, 2);
plot(reject_x, ';null test;', bayes_reject_x, ';Bayes test;')
title("Rejection of null hypothesis for Bernoulli(0.5)");
matlab2tikz("p-value-example-null-posterior.tikz", 'height', '\fheight', 'width', '\fwidth' );


figure(5);
bayes_reject_y = mean(posterior_y < 0.5, 2);
plot(reject_y, ';null test;', bayes_reject_y, ';Bayes test;')
title("Rejection of null hypothesis for Bernoulli(0.45)");
matlab2tikz("p-value-example-true-posterior.tikz", 'height', '\fheight', 'width', '\fwidth' );
