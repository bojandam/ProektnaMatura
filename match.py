from agent import Agent
from grid import Grid, Results


class Match:
    def __init__(
        self, player1: Agent = Agent(), player2: Agent = Agent(), grid: Grid = Grid()
    ):
        self.player1 = player1
        self.player2 = player2
        self.grid = grid
        self.resultMap = {
            Results.Won_X: (1, -1),
            Results.Won_0: (-1, 1),
            Results.Tie: (0, 0),
            Results.Failed_X: (-3, 0.5),
            Results.Failed_0: (0.5, -3),
        }
        self.result = (0, 0)

    def predict_to_point(self, OutputLayer: list):
        i = OutputLayer.index(max(OutputLayer))
        return (i // 3, i % 3)

    def move(self, player: Agent, prt: bool = False):
        InputLayer = self.grid.getX() if self.grid.turn == "X" else self.grid.getY()
        pos = self.predict_to_point(player.predict(InputLayer=InputLayer))
        if prt:
            print(pos)
        if self.grid.place(pos):  # True if pos is a legal placement
            self.grid.check()

    def play(self, turn="X", prt: bool = False):
        self.grid.__init__()
        self.grid.turn = turn
        if prt:
            print(self.grid)
        while not self.grid.done():
            self.move(self.player1 if self.grid.turn == "X" else self.player2)
            if prt:
                print(self.grid)
        return self.resultMap[self.grid.result]

    def getResult(self, prt: bool = False):
        self.result = tuple(map(sum, zip(self.result, self.play("X", prt=prt))))
        self.result = tuple(map(sum, zip(self.result, self.play("0", prt=prt))))
        self.result = tuple(map(sum, zip(self.result, self.play("X", prt=prt))))
        return (self.result[0], self.player1, self.result[1], self.player2)


class Tournament:
    def __init__(self, pow_of_two=4):
        self.agents = [(Agent(), Agent()) for i in range(int(pow(2, pow_of_two)))]
        self.ranking = []

    def rank(self, agents: list = None, prt: bool = False):
        if agents is None:
            agents = self.agents[:]
        if len(agents) == 1 and agents[0] is not tuple:
            self.ranking.extend(agents)
            return
        results = [Match(P1, P2).getResult(prt=prt) for P1, P2 in agents]
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


if __name__ == "__main__":
    turnament = Tournament(10)
    turnament.rank()
    # Match(turnament.ranking[0], turnament.ranking[1]).getResult(prt=True)
    print((turnament.ranking[0], turnament.ranking[1]))
