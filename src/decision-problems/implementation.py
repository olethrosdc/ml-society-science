import skeleton
from sklearn.linear_model import LogisticRegression

class ScikitLearnModel(skeleton.Model):
    def __init__(self):
        # We initialize with very weak regularization not to throw
        # off the testing engine. This might not be what students should/
        # will want to do
        self.model = LogisticRegression(C=100)
    def fit(self, X, y):
        self.model.fit(X, y)
        return self
    def get_class_probability(self, X):
        return self.model.predict_proba(X)
