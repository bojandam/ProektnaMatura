from oldAgent import Agent
from typing import List, Tuple

from random import randint, random, seed
from time import time


def Mix(geneA: list, geneB: list) -> Tuple[list, list]:
    i = randint(1, len(geneA) - 1)
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


def reproduce(
    agents: List[Agent],  # A ranked list (0 best) of agents
    Keep: int,  # How many of the original to keep
    Mixes: int,  # How many times to do of each type of action
    Selections: int,
    SingleMutations: int,
    SlabMutations: int,
    RainMutations: int,
):
    seed(time())
    genes = [agent.flattened() for agent in agents]
    Len = len(agents)
    next_gen_genes = genes[:Keep]
    for i in range(Mixes):
        next_gen_genes.extend(Mix(genes[randint(0, Keep)], genes[randint(0, Keep)]))
    for i in range(Selections):
        next_gen_genes.extend(
            Selection(genes[randint(0, Keep)], genes[randint(0, Keep)])
        )
    for i in range(SingleMutations):
        next_gen_genes.append(SingleMutation(genes[randint(0, Keep)]))
    for i in range(SlabMutations):
        next_gen_genes.append(SlabMutation(genes[randint(0, Keep)]))
    for i in range(RainMutations):
        next_gen_genes.append(RainMutation(genes[randint(0, Keep)]))

    if len(next_gen_genes) > Len:
        next_gen_genes = next_gen_genes[:Len]
    next_gen = [Agent() for i in range(Len)]
    for i in range(len(next_gen_genes)):
        next_gen[i].construct(next_gen_genes[i])
    return [(next_gen[i], next_gen[i + 1]) for i in range(0, Len, 2)]


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
