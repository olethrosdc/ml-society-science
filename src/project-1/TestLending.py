import pandas

features = ['checking account balance', 'duration', 'credit history',
            'purpose', 'amount', 'savings', 'employment', 'installment',
            'marital status', 'other debtors', 'residence time',
            'property', 'age', 'other installments', 'housing', 'credits',
            'job', 'persons', 'phone', 'foreign']
target = 'repaid'
df = pandas.read_csv('../../data/credit/german.data', sep=' ',
                     names=features+[target])
import matplotlib.pyplot as plt
numerical_features = ['age', 'residence time', 'installment', 'amount', 'duration', 'persons', 'credits']
quantitative_features = list(filter(lambda x: x not in numerical_features, features))
X = pandas.get_dummies(df, columns=quantitative_features, drop_first=True)
encoded_features = list(filter(lambda x: x != target, X.columns))


### Setup model
#import LogisticBanker
#decision_maker = LogisticBanker()
import random_banker
decision_maker = random_banker.RandomBanker()
interest_rate = 0.05
decision_maker.set_interest_rate(interest_rate)
decision_maker.fit(X[encoded_features], X[target])
n_test_examples = 100
utiity = 0

for t in range(n_test_examples):
    action = decision_maker.get_best_action(X[encoded_features].iloc[t])
    default = X[target].iloc[t] # assume the labels are correct
    duration = X['duration'].iloc[t]
    amount = X['amount'].iloc[t]
    # If we don't grant the loan then nothing happens
    if (action==1):
        if (default):
            utility -= amount*(pow(1 + interest_rate) - 1)
        else:    
            utility += amount*(pow(1 + interest_rate) - 1)
    




