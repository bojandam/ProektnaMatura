import numpy as np
from random import random, seed
from time import time

from sklearn.preprocessing import minmax_scale


class Agent:
    # LAYER_SIZES = [9, 16, 8, 9]
    LAYER_SIZES = [9, 8, 4, 9]
    indices = []

    def __init__(self):
        Len = 0
        seed(time())
        if Agent.indices == []:
            Agent.indices = [0] * len(self.LAYER_SIZES)
            for i in range(1, len(Agent.LAYER_SIZES)):
                Len += (Agent.LAYER_SIZES[i - 1] + 1) * Agent.LAYER_SIZES[i]
                Agent.indices[i] = Len

        self.gene = [random() * 2 - 1 for i in range(Agent.indices[-1])]

        self.Played = 0
        self.Points = 0

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
                        self.indices[i]
                        + j * (self.LAYER_SIZES[i] + 1) : self.indices[i]
                        + (j + 1) * (self.LAYER_SIZES[i] + 1)
                    ],
                    range(self.LAYER_SIZES[i] + 1),
                ):
                    ResultLayer[j] += w * ActiveLayer[k]
                ResultLayer[j] = float(self.activate(ResultLayer[j]))
            ActiveLayer = ResultLayer[:]
        return ActiveLayer

    def flattened(self):
        return self.gene

    def construct(self, flat: list):
        if self.gene != flat:
            self.Played = 0
            self.Loses = 0
        self.gene = flat

    def __str__(self):
        return f"{self.gene} -  {self.indices}  - {len(self.gene)}"


def fitness(agent: Agent):
    return (agent.Points) / (2 * agent.Played)


if __name__ == "__main__":
    Test = Agent()
    print(Test)
    print()
    print([round(el, 2) for el in Test.predict([0, 1, 0, -1, -1, 1, 0, -1, 0])])
