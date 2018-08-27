class Model(object):
    def fit(self, X, y):
        raise NotImplementedError()
    def get_decision_probability(self, X):
        raise NotImplementedError()
    def get_class_probability(self, X):
        raise NotImplementedError()

class ScikitLearnModel(Model):
    pass

class StatsModelsModel(Model):
    pass

