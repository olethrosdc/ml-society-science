# Run these from src/decision-problems, using
#
# python -m unittest tests/model_tests.py

import unittest
from implementation import ScikitLearnModel

class SklearnModelTests(unittest.TestCase):

    def test_fit_predict(self):
        '''Fitting a simple two-class linear model and checking correctness.'''
        X = [[i] for i in range(10)]
        y = [0]*5 + [1]*5
        model = ScikitLearnModel()
        fitted_model = model.fit(X, y)
        probs = fitted_model.get_class_probability(X)
        for i, p in enumerate(probs):
            prob_zero, prob_one = p
            if i < 5:
                self.assertGreater(prob_zero, 0.5)
            else:
                self.assertGreater(prob_one, 0.5)
