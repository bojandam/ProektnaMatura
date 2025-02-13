from oldAgent import Agent
from typing import List, Tuple

from random import randint, random, seed
from time import time


def Mutate(geneA: list, geneB: list) -> Tuple[list, list]:
    i = randint(1, len(geneA) - 1)
    print(i)
    return (geneA[:i] + geneB[i:], geneB[:i] + geneA[i:])


def Selection(geneA: list, geneB: list) -> Tuple[list, list]:
    i = randint(1, len(geneA) - 2)
    j = randint(i, len(geneA) - 1)
    return (geneA[:i] + geneB[i:j] + geneA[j:], geneB[:i] + geneA[i:j] + geneB[j:])


def SingleMutation(gene: list) -> list:  # a single value gets mutated
    i = randint(1, len(gene) - 1)
    rez = gene[:]
    rez[i] = random() * 2 - 1
    return rez


def SlabMutation(gene) -> list:  # a range [i,j) gets mutated
    i = randint(0, len(gene) - 1)
    j = randint(i, len(gene))
    return [
        gene[k] if k not in range(i, j) else (random() * 2 - 1)
        for k in range(len(gene))
    ]


def RainMutation(gene):  # multiple mutatuions, up to a sixth of the original gene
    ammount = randint(4, len(gene) // 6)
    rez = gene[:]
    for i in range(ammount):
        rez = SingleMutation(rez)
    return rez


def reproduce(agents: List[Agent]):
    seed(time(0))
    genes = [agent.flattened() for agent in agents]
    Len = len(agents)


if __name__ == "__main__":
    left = list(range(10))
    right = ["b"] * 30
    rez = []
    # print(Mutate(left, right))
    # print(Selection(left, right))
    # print(SingleMutation(left))
    # print(SlabMutation(right))
    print(RainMutation(right))
    # rez.extend(Mutate(left, right))
    # rez.extend(Selection(left, right))
    # rez.append(SingleMutation(left))
    # rez.append(SlabMutation(right))
    rez.append(RainMutation(right))
    print(rez)
