import numpy as np
from random import random, seed, randint
from time import time

from sklearn.neural_network import MLPClassifier


seed(time())


class Agent:
    LAYER_SIZES = [9, 16, 8, 9]
    # LAYER_SIZES = [2, 3, 3, 2]

    def __init__(self):
        self.mlp = MLPClassifier(hidden_layer_sizes=self.LAYER_SIZES)
        self.mlp.fit(  # generates random neural network
            [[0] * self.LAYER_SIZES[0]],
            [0],  # randint(0, 9)
        )  # random enough hopefully (random first move)

        # for constructing the gene structure again (un-flattening)
        self.shapes = [
            arr.shape for arr in self.mlp.coefs_
        ]  # gets the dimentions of matrix of weights for each two layers (effectively : (lyr_size[i],lyr_size[i+1]))
        self.chunk_lens = [
            x * y for x, y in self.shapes
        ]  # how many elements of the array go in each matrix
        self.chunk_idexes = [
            sum(self.chunk_lens[:i]) for i in range(len(self.chunk_lens) + 1)
        ]  # stores the beginning indices of the abve-mentioned chunks

    def construct(self, flat: list):  # opposite of flatten
        self.mlp.coefs_ = [
            np.array(flat[self.chunk_idexes[i] : self.chunk_idexes[i + 1]]).reshape(
                self.shapes[i]
            )
            for i in range(len(self.chunk_idexes) - 1)
        ]

    def flattened(self):
        return [x for column in self.mlp.coefs_ for row in column for x in row]


def flatten3d(arr: list):
    return [x for column in arr for row in column for x in row]


if __name__ == "__main__":
    agent = Agent()
    # print(agent.flattened())
    agent1 = Agent()
    # print(agent1.flattened())
    print()
    print()
    print(agent1.flattened() == agent.flattened())
    print(agent.mlp.predict([[0] * 9]))
    print(agent1.mlp.predict([[0] * 9]))
