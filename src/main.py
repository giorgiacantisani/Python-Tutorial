# std imports
from numpy.random import permutation
from sklearn import datasets

# my imports
from models.predict_model import predict
from models.train_model import train

#...add here the new nice imports and add the followings
from sacred import Experiment
ex = Experiment('iris_svm') # id of the experiments

@ex.config
def cfg():
    C = 2
    gamma = 0.7

@ex.automain
def run(_run, C, gamma):
    iris = datasets.load_iris()
    per = permutation(iris.target.size)
    iris.data = iris.data[per]
    iris.target = iris.target[per]
    model = train(iris.data[:90], iris.target[:90], C, gamma)
    score = predict(model, iris.data[90:], iris.target[90:])
    print(score)

    # loss
    counter = 0
    while counter < 20:
        counter+=1
        value = counter
        # This will add an entry for training.loss metric in every second iteration.
        # The resulting sequence of steps for training.loss will be 0, 2, 4, ...
        if counter % 2 == 0:
            _run.log_scalar("training.loss", value * 1.5, counter)
        # Implicit step counter (0, 1, 2, 3, ...)
        # incremented with each call for training.accuracy:
        _run.log_scalar("training.accuracy", value * 2)
        # Another option is to use the Experiment object (must be running)
        # The training.diff has its own step counter (0, 1, 2, ...) too
        ex.log_scalar("training.diff", value * 2)
    return score


