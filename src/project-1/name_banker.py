import numpy as np
from sklearn.naive_bayes import MultinomialNB

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
        action = expected_utility()
        return self.clf.predict_proba(x)


    # THe expected utility of granting the loan or not. Here there are two actions:
    # action = 0 do not grant the loan
    # action = 1 grant the loan
    #
    # Make sure that you extract the length_of_loan from the
    # 2nd attribute of x. Then the return if the loan is paid off to you is amount_of_loan*(1 + rate)^length_of_loan
    # The return if the loan is not paid off is -amount_of_loan.
    
    def expected_utility(self, x, action):
        print("Expected utility: Not implemented")
        if self.predict_proba(x) == 0:
            return 0
        else:
            return x[4] * (1 + self.rate)**x[1]

    # Return the best action. This is normally the one that maximises expected utility.
    # However, you are allowed to deviate from this if you can justify the reason.
    def get_best_action(self, x):
        action = self.predict_proba(x)
        return action
        