import numpy as np
from random import seed, randint
from time import time

from sklearn.neural_network import MLPRegressor
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

seed(time())


@ignore_warnings(category=ConvergenceWarning)
class Agent:
    LAYER_SIZES = [9, 16, 8, 9]
    # LAYER_SIZES = [2, 3, 3, 2]

    def __init__(self):
        self.mlp = MLPRegressor(hidden_layer_sizes=self.LAYER_SIZES[1:-1])
        self.mlp.fit(
            [[0] * self.LAYER_SIZES[0]],
            [[randint(0, 9) for i in range(self.LAYER_SIZES[-1])]],
        )

        # for constructing the gene structure again (un-flattening)
        self.shapes = [arr.shape for arr in self.mlp.coefs_]
        self.chunk_lens = [x * y for x, y in self.shapes]
        self.chunk_idexes = [
            sum(self.chunk_lens[:i]) for i in range(len(self.chunk_lens) + 1)
        ]
        self.bias_indexes = [
            self.chunk_idexes[-1] + sum((self.LAYER_SIZES[1:])[:i])
            for i in range(len(self.LAYER_SIZES[1:]) + 1)
        ]

    def construct(self, flat: list):  # opposite of flatten
        self.mlp.coefs_ = [
            np.array(flat[self.chunk_idexes[i] : self.chunk_idexes[i + 1]]).reshape(
                self.shapes[i]
            )
            for i in range(len(self.chunk_idexes) - 1)
        ]

        self.mlp.intercepts_ = [
            np.array(flat[self.bias_indexes[i] : self.bias_indexes[i + 1]]).reshape(
                ((self.LAYER_SIZES[1:])[i])
            )
            for i in range(len(self.bias_indexes) - 1)
        ]

    def flattened(self):
        coefs = [x for column in self.mlp.coefs_ for row in column for x in row]
        biases = [x for col in self.mlp.intercepts_ for x in col]
        return coefs + biases

    def predict(self, InputLayer: list):
        return [x for x in self.mlp.predict([InputLayer])[0]]


def flatten3d(arr: list):
    return [x for column in arr for row in column for x in row]


if __name__ == "__main__":

    ammount = 100
    start = time()
    for i in range(ammount):
        Agent().predict([0] * 9)
    end = time()
    delta = end - start
    print(delta / ammount)
