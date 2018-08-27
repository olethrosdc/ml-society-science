import unittest
from implementation import ScikitLearnModel

class SklearnModelTests(unittest.TestCase):

    def test_fit_predict(self):
        X = [[i] for i in range(10)]
        y = [0]*5 + [1]*5
        model = ScikitLearnModel()
        fitted_model = model.fit(X, y)
        probs = fitted_model.predict_probabilities(X)
        for i, p in enumerate(probs):
            if i <= 5:
                self.assertGreater(0.5, p)
            else:
                self.assertGreater(p, 0.5)
