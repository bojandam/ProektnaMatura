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
            Results.Failed_X: (-3, 1),
            Results.Failed_0: (1, -3),
        }

    def predict_to_point(self, OutputLayer: list):
        i = OutputLayer.index(max(OutputLayer))
        return (i // 3, i % 3)

    def move(self, player: Agent):
        InputLayer = self.grid.getX() if self.grid.turn == "X" else self.grid.getY()
        pos = self.predict_to_point(player.predict(InputLayer=InputLayer))
        print(pos)
        if self.grid.place(pos):  # True if pos is a legal placement
            self.grid.check()

    def play(self):
        print(self.grid)
        while not self.grid.done():
            self.move(self.player1 if self.grid.turn == "X" else self.player2)
            print(self.grid)
        return self.resultMap[self.grid.result]


if __name__ == "__main__":
    test = Match()
    test.play()
