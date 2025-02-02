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

    def move(self, player: Agent, print: bool = False):
        InputLayer = self.grid.getX() if self.grid.turn == "X" else self.grid.getY()
        pos = self.predict_to_point(player.predict(InputLayer=InputLayer))
        if print:
            print(pos)
        if self.grid.place(pos):  # True if pos is a legal placement
            self.grid.check()

    def play(self, turn="X", print: bool = False):
        self.grid.__init__()
        self.grid.turn = turn
        if print:
            print(self.grid)
        while not self.grid.done():
            self.move(self.player1 if self.grid.turn == "X" else self.player2)
            if print:
                print(self.grid)
        return self.resultMap[self.grid.result]

    def getResult(self):
        self.result = tuple(map(sum, zip(self.result, self.play())))
        self.result = tuple(map(sum, zip(self.result, self.play("0"))))
        self.result = tuple(map(sum, zip(self.result, self.play())))
        return self.result


if __name__ == "__main__":
    # print(Match().getResult())
    agents = [(Agent(), Agent()) for i in range(250)]
    results = [Match(P1, P2).getResult() for P1, P2 in agents]
    print(max(results))
