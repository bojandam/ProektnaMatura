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
        tempRez = (
            self.resultMap[self.grid.result][0] - self.errsP1,
            self.resultMap[self.grid.result][1] - self.errsP2,
        )

        return tempRez

    def getResult(self, prt: bool = False):
        self.result = tuple(map(sum, zip(self.result, self.play("X", prt=prt))))
        self.result = tuple(map(sum, zip(self.result, self.play("0", prt=prt))))
        self.result = tuple(map(sum, zip(self.result, self.play("X", prt=prt))))
        return (self.result[0], self.player1, self.result[1], self.player2)


calls = 0


class Tournament:
    def __init__(self, pow_of_two=4):
        self.agents = [(Agent(), Agent()) for i in range(int(pow(2, pow_of_two)))]
        self.ranking = []

    def rank(self, agents: list = None, prt: bool = False):
        calls += 1
        print("call", calls, ":", len(agents))
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


if __name__ == "__main__":
    turnament = Tournament(12)
    turnament.rank()
    print()
    print("ranked")
    # Match(turnament.ranking[0], turnament.ranking[1]).getResult(prt=True)
    print(Match(turnament.ranking[0], turnament.ranking[1]).getResult(True))
