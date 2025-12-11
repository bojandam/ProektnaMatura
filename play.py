from oldAgent import Agent
from match import Match
from grid import Grid
import Best
import importlib


def human_play(grid):
    print(grid)
    x, y = map(int, input().split())
    while not grid.place((x, y)):
        print("Invalid input, try again: ")
        x, y = map(int, input().split())
    # print(grid)


if __name__ == "__main__":
    importlib.reload(Best)

    AI: Agent = Agent()
    AI.construct(Best.BestAgent)
    grid: Grid = Grid()
    runda: Match = Match(None, AI, grid)
    order = [lambda: human_play(grid=grid), lambda: runda.move(AI, False)]
    index = 0 if input("Do you wanna go first?(Y/N):").capitalize() == "Y" else 1

    while not grid.done():
        (order[index])()
        index += 1
        index %= 2
    print(grid)
