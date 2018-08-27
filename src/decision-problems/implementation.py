import skeleton
from sklearn.linear_model import LogisticRegression

class ScikitLearnModel(skeleton.Model):
    def __init__(self):
        self.model = LogisticRegression()
    def fit(self, X, y):
        self.model.fit(X, y)
        return self
