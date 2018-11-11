import numpy as np
import pandas
import matplotlib.pyplot as plt

def simple_reward_function(action, outcome):
    return outcome


def test_policy(generator, policy, reward_function, T):
    policy.set_reward(reward_function)
    u = 0
    r = np.zeros(T)
    for t in range(T):
        a = policy.recommend()
        y = generator.generate(a)
        r[t] = y
        u += r[t]
        policy.observe(action=a, outcome=y)
    print("Total reward: ", u)
    return r

n_actions = 16
n_outcomes = 2
import average_bandit
average_policy = average_bandit.AverageBandit(n_actions, n_outcomes, 0)
average_policy_2 = average_bandit.AverageBandit(n_actions, n_outcomes, 10)
import softmax_bandit
softmax_policy = softmax_bandit.SoftmaxBandit(n_actions, n_outcomes, 1)
import thompson_bandit
thompson_policy = thompson_bandit.ThompsonBandit(n_actions, n_outcomes, 1, 1)



T = 10000
import bernoulli_bandit
generator = bernoulli_bandit.BernoulliBandit(n_actions)
average_result = test_policy(generator, average_policy, simple_reward_function, T)
#average_result2 = test_policy(generator, average_policy_2, simple_reward_function, T)
softmax_result = test_policy(generator, softmax_policy, simple_reward_function, T)
thompson_result = test_policy(generator, thompson_policy, simple_reward_function, T)
results = pandas.DataFrame({'Thompson': thompson_result, 'Softmax': softmax_result, 'Linear': average_result})

results.rolling(window=int(np.ceil(np.sqrt(T)))).sum().plot()
plt.show()
