import numpy as np
from random import random, seed
from time import time

from sklearn.preprocessing import minmax_scale


class Agent:
    LAYER_SIZES = [9, 16, 8, 9]

    def generateGene(self):
        Len = 0
        seed(time())

        for i in range(1, len(self.LAYER_SIZES)):
            Len += (self.LAYER_SIZES[i - 1] + 1) * self.LAYER_SIZES[i]
            self.indices[i] = Len
        self.indices = self.indices[:-1]

        self.gene = [random() for i in range(Len)]
        self.gene = list(minmax_scale(self.gene, (-1, 1)))
        self.gene = [float(el) for el in self.gene]

    def __init__(self, gene=None, indices=None):
        self.indices = [0] * len(self.LAYER_SIZES)
        if gene:
            self.gene = gene
            self.indices = indices
        else:
            self.generateGene()

    def activate(self, val: float) -> float:
        return 1 / (1 + np.exp(-val))

    def predict(self, InputLayer: list):
        ActiveLayer = InputLayer[:]
        for i in range(len(self.LAYER_SIZES) - 1):
            ActiveLayer.append(1)
            ResultLayer = [0] * self.LAYER_SIZES[i + 1]

            for j in range(self.LAYER_SIZES[i + 1]):
                for w, k in zip(
                    self.gene[
                        self.indices[i] + j * (self.LAYER_SIZES[i] + 1) : self.indices[
                            i
                        ]
                        + (j + 1) * (self.LAYER_SIZES[i] + 1)
                    ],
                    range(self.LAYER_SIZES[i] + 1),
                ):
                    ResultLayer[j] += w * ActiveLayer[k]
                ResultLayer[j] = float(self.activate(ResultLayer[j]))
            ActiveLayer = ResultLayer[:]
        return ActiveLayer

    def __str__(self):
        return f"{self.gene} -  {self.indices}  - {len(self.gene)}"


if __name__ == "__main__":
    Test = Agent()
    print()
    print([round(el, 2) for el in Test.predict([0, 0, 0, 0, 0, 0, 0, 0, 0])])
    Other = Agent()
    print([round(el, 2) for el in Agent().predict([0, 0, 0, 0, 0, 0, 0, 0, 0])])
    print([round(el, 2) for el in Agent().predict([0, 0, 0, 0, 0, 0, 0, 0, 0])])
    print([round(el, 2) for el in Agent().predict([0, 0, 0, 0, 0, 0, 0, 0, 0])])
    print([round(el, 2) for el in Agent().predict([0, 0, 0, 0, 0, 0, 0, 0, 0])])
    print([round(el, 2) for el in Agent().predict([0, 0, 0, 0, 0, 0, 0, 0, 0])])
    print([round(el, 2) for el in Agent().predict([0, 0, 0, 0, 0, 0, 0, 0, 0])])
    print([round(el, 2) for el in Agent().predict([0, 0, 0, 0, 0, 0, 0, 0, 0])])
