import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

class Nenuro:
    def __init__(self, weight, xingcan_bias):
        #self.half = bias + weight
        self.weight = weight
        self.bias = xingcan_bias

    def feedforward(self, inputs):
        total = np.dot(self.weight, inputs) + self.bias
        return sigmoid(total)

if __name__ == '__main__':
    weight = np.array([1, 3])
    shican_bias = 1
    n = Nenuro(weight, shican_bias)
    x = np.array([0.4, 0.5])
    print(n.feedforward(x))







