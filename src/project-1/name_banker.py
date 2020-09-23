import numpy as np
from sklearn.naive_bayes import MultinomialNB
np.seterr(all='ignore')
class NameBanker:
    
    # Fit the model to the data.  You can use any model you like to do
    # the fit, however you should be able to predict all class
    # probabilities
    def fit(self, X, y):
        self.data = [X, y]
        self.clf = MultinomialNB()
        self.clf.fit(X, y)
        return self.clf
        

    # set the interest rate
    def set_interest_rate(self, rate):
        self.rate = rate
        return

    # Predict the probability of failure for a specific person with data x
    def predict_proba(self, x):
        x = [x]
        predict = self.clf.predict_proba(x)
        return predict[0][0]


    # THe expected utility of granting the loan or not. Here there are two actions:
    # action = 0 do not grant the loan
    # action = 1 grant the loan
    #
    # Make sure that you extract the length_of_loan from the
    # 2nd attribute of x. Then the return if the loan is paid off to you is amount_of_loan*(1 + rate)^length_of_loan
    # The return if the loan is not paid off is -amount_of_loan.
    
    def expected_utility(self, x):
        predict = self.predict_proba(x)
        return predict * x[4] * (np.power(1 + self.rate, x[1]) - 1) - (1 - predict)*x[4]

    # Return the best action. This is normally the one that maximises expected utility.
    # However, you are allowed to deviate from this if you can justify the reason.
    def get_best_action(self, x):
        if self.expected_utility(x) > 0:
            return 1
        else:
            return 0