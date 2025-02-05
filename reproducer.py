from agent import Agent
from typing import List

from random import random, seed
from time import time


def reproduce(agents: List[Agent]):
    seed(time(0))
    indecies = agents[0].indices
    genes = [agent.gene for agent in agents]
