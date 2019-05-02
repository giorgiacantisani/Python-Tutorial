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
    C = 1.0
    gamma = 0.7

@ex.automain
def run(C, gamma):
    iris = datasets.load_iris()
    per = permutation(iris.target.size)
    iris.data = iris.data[per]
    iris.target = iris.target[per]
    model = train(iris.data[:90], iris.target[:90], C, gamma)
    score = predict(model, iris.data[90:], iris.target[90:])
    return score


