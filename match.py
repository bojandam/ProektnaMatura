from oldAgent import Agent
from grid import Grid, Results
from reproducer import reproduce
from functools import cmp_to_key


class Match:
    def __init__(
        self, player1: Agent = Agent(), player2: Agent = Agent(), grid: Grid = Grid()
    ):
        self.player1 = player1
        self.player2 = player2
        self.grid = grid
        self.resultMap = {
            Results.Won_X: (2, -2),
            Results.Won_0: (-2, 2),
            Results.Tie: (1, 1),
        }
        self.errsP1 = 0
        self.errsP2 = 0
        self.result = (0, 0)

    # def predict_to_point(self, OutputLayer: list):
    #     i = OutputLayer.index(max(OutputLayer))
    #     return (i // 3, i % 3)

    def move(self, player: Agent, prt: bool = False):
        InputLayer = self.grid.getX() if self.grid.turn == "X" else self.grid.getY()
        predicted = player.predict(InputLayer=InputLayer)

        i = predicted.index(max(predicted))
        pos = (i // 3, i % 3)

        if prt:
            print(pos)
        while not self.grid.place(pos):  # True if pos is a legal placement
            if self.grid.turn == "X":
                self.errsP1 += 1
            else:
                self.errsP2 += 1

            predicted[i] = min(predicted) - 1  # It will never get picked again

            i = predicted.index(max(predicted))
            pos = (i // 3, i % 3)
        # self.grid.check()

    def play(self, turn="X", prt: bool = False):
        self.grid.__init__()
        self.grid.turn = turn

        while not self.grid.done():
            self.move(self.player1 if self.grid.turn == "X" else self.player2)
            if prt:
                print(self.grid)
        tempRez = (
            self.resultMap[self.grid.result][0] - self.errsP1,
            self.resultMap[self.grid.result][1] - self.errsP2,
        )

        return tempRez

    def getResult(self, prt: bool = False):
        self.result = tuple(map(sum, zip(self.result, self.play("X", prt=prt))))
        self.result = tuple(map(sum, zip(self.result, self.play("0", prt=prt))))
        # self.result = tuple(map(sum, zip(self.result, self.play("X", prt=prt))))
        return (self.result[0], self.player1, self.result[1], self.player2)


def compare(L, R):
    l, p1, r, p2 = Match(L, R).getResult()
    if l > r:
        return 1
    elif l == r:
        return 0
    else:
        return -1


class Tournament:
    def __init__(self, pow_of_two_OR_agents=4):
        if type(pow_of_two_OR_agents) == int:
            self.agents = [  # pow_of_two_OR_agents is a power of 2
                (Agent(), Agent()) for i in range(int(pow(2, pow_of_two_OR_agents)))
            ]
        else:  # pow_of_two_OR_agents is a list of agents
            self.agents = pow_of_two_OR_agents
        self.ranking = []

    def rank(self):
        self.ranking = sorted(
            [x for y in self.agents for x in y], key=cmp_to_key(compare)
        )

    def rankOld(self, agents: list = None, prt: bool = False):
        if agents is None:
            agents = self.agents[:]
        if len(agents) == 1 and type(agents[0]) != tuple:
            self.ranking.extend(agents)
            return
        results = [Match(P1, P2).getResult(prt=prt) for P1, P2 in agents]
        if len(agents) == 1:
            r1, p1, r2, p2 = results[0]
            self.rank([p1 if r1 > r2 else p2])
            self.rank([p1 if r1 <= r2 else p2])
            return
        winers = [
            (p1 if r1 > r2 else p2, p3 if r3 > r4 else p4)
            for (r1, p1, r2, p2, r3, p3, r4, p4) in [
                results[i] + results[i + 1] for i in range(0, len(results), 2)
            ]
        ]
        losers = [
            (p1 if r1 <= r2 else p2, p3 if r3 <= r4 else p4)
            for (r1, p1, r2, p2, r3, p3, r4, p4) in [
                results[i] + results[i + 1] for i in range(0, len(results), 2)
            ]
        ]
        self.rank(winers)
        self.rank(losers)


Data = []


def start(n=5):
    n = 5
    m = int(pow(2, n))
    turnament = Tournament(n - 1)

    while True:
        for i in range(50):
            turnament.rank()
            Data.append(
                [
                    Match(turnament.ranking[i], turnament.ranking[i + 1]).getResult(
                        False
                    )
                    for i in range(0, len(turnament.ranking), 2)
                ]
            )
            print(
                Match(turnament.ranking[0], turnament.ranking[1]).getResult(
                    True if i == 49 else False
                )
            )
            turnament = Tournament(
                reproduce(
                    turnament.ranking,
                    Keep=m // 2 + m // 32,
                    Mixes=m // 16,
                    Selections=m // 16,
                    SingleMutations=m // 16,
                    SlabMutations=m // 32,
                    RainMutations=m // 16,
                )
            )


if __name__ == "__main__":
    n = 5
    start(n)
    print(Data)
