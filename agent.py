import numpy as np
from random import random, seed, randint
from time import time

from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

seed(time())


@ignore_warnings(category=ConvergenceWarning)
class Agent:
    LAYER_SIZES = [9, 16, 8, 9]
    # LAYER_SIZES = [2, 3, 3, 2]

    def __init__(self):
        # self.mlp = MLPClassifier(hidden_layer_sizes=self.LAYER_SIZES)
        self.mlp = MLPRegressor(hidden_layer_sizes=Agent.LAYER_SIZES[1:-1])

        # self.mlp.fit(  # generates random neural network
        #     [[0] * self.LAYER_SIZES[0]], [randint(0, 9)]
        # )  # random enough hopefully (random first move)
        self.mlp.fit(
            [[0] * Agent.LAYER_SIZES[0]],
            [[randint(0, 9) for i in range(Agent.LAYER_SIZES[-1])]],
        )

        # for constructing the gene structure again (un-flattening)

        self.shapes = [arr.shape for arr in self.mlp.coefs_]
        # gets the dimentions of matrix of weights for each two layers (effectively : (lyr_size[i],lyr_size[i+1]))
        self.chunk_lens = [x * y for x, y in self.shapes]
        # how many elements of the array go in each matrix
        self.chunk_idexes = [
            sum(self.chunk_lens[:i]) for i in range(len(self.chunk_lens) + 1)
        ]
        # stores the beginning indices of the abve-mentioned chunks
        # self.bias_indexes = [
        #     self.chunk_idexes[-1] + sum((self.LAYER_SIZES + [1])[:i])
        #     for i in range(len(self.LAYER_SIZES + [1]) + 1)
        # ]
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
    # mlp = MLPRegressor(hidden_layer_sizes=Agent.LAYER_SIZES[1:-1])
    # mlp.fit(
    #     [[0] * Agent.LAYER_SIZES[0]],
    #     [[randint(0, 9) for i in range(Agent.LAYER_SIZES[-1])]],
    # )
    # print(mlp.n_outputs_)
    # print(mlp.predict([[0] * Agent.LAYER_SIZES[0]]))
    # shapes = [arr.shape for arr in mlp.coefs_]
    # chunk_lens = [x * y for x, y in shapes]
    # chunk_idexes = [sum(chunk_lens[:i]) for i in range(len(chunk_lens) + 1)]
    # print(shapes)
    # print(chunk_lens)
    # print(chunk_idexes)
    # print(len(flatten3d(mlp.coefs_)))
    # bias_indexes = [
    #     chunk_idexes[-1] + sum((Agent.LAYER_SIZES[1:])[:i])
    #     for i in range(len(Agent.LAYER_SIZES[1:]) + 1)
    # ]
    # print(bias_indexes)
    # print(mlp.intercepts_)
    # biases = [x for col in mlp.intercepts_ for x in col]
    # flat = flatten3d(mlp.coefs_) + biases
    # print(biases)
    # print(
    #     [
    #         np.array(flat[bias_indexes[i] : bias_indexes[i + 1]]).reshape(
    #             ((Agent.LAYER_SIZES[1:])[i])
    #         )
    #         for i in range(len(bias_indexes) - 1)
    #     ]
    # )
    # print()
    # print(mlp.coefs_)
    # print(
    #     [
    #         np.array(flat[chunk_idexes[i] : chunk_idexes[i + 1]]).reshape(shapes[i])
    #         for i in range(len(chunk_idexes) - 1)
    #     ]
    # )
    agent = Agent()
    print(agent.predict([0] * 9))
