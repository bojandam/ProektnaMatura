from enum import Enum


class Results(Enum):
    Won_X = "X"
    Won_0 = "0"
    Tie = "Tie"
    Ongoing = None


class Grid:
    def __init__(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.result = Results.Ongoing
        self.Values = [1, -1, 0]  # For X: 1 if X, -1 if 0, 0 if Null, swaped for 0
        # self.turnsX = 0
        # self.turnsY = 0

    def change_turn(self):
        if self.turn == "X":
            self.turn = "0"
            # self.turnsX += 1
        else:
            self.turn = "X"
            # self.turnsY += 1

    def place(self, position):
        if (
            position[0] in range(3)
            and position[1] in range(3)
            and self.grid[position[0]][position[1]] == " "
        ):
            self.grid[position[0]][position[1]] = self.turn
            self.change_turn()
            self.check()
            return True
        return False

    def full(self):
        for row in self.grid:
            for x in row:
                if x == " ":
                    return False
        return True

    def check(self):
        if not self.done():
            lines = [r[:] for r in self.grid]
            for i in range(3):
                lines.append([r[i] for r in self.grid])
            lines.append([self.grid[i][i] for i in range(3)])
            lines.append([self.grid[i][2 - i] for i in range(3)])
            if ["X", "X", "X"] in lines:
                self.result = Results.Won_X
            elif ["0", "0", "0"] in lines:
                self.result = Results.Won_0
            elif self.full():
                self.result = Results.Tie

    def done(self):
        return self.result is not Results.Ongoing

    def GridToRow(self):
        arr = []
        for row in self.grid:
            arr.extend(row)
        return arr

    def getX(self):
        arr = self.GridToRow()
        return [
            (
                self.Values[0]
                if X == "X"
                else (self.Values[1] if X == "0" else self.Values[2])
            )
            for X in arr
        ]

    def getY(self):
        arr = self.GridToRow()
        return [
            (
                self.Values[1]
                if X == "X"
                else (self.Values[0] if X == "0" else self.Values[2])
            )
            for X in arr
        ]

    def __str__(self):
        return (
            f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} \n"
            f"---+---+---\n"
            f" {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} \n"
            f"---+---+---\n"
            f" {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} \n"
            f"\n"
            f"--- {self.result.value} ---\n"
        )


if __name__ == "__main__":
    grid = Grid()
    print(grid)
    while not grid.done():
        x, y = map(int, input().split())
        while not grid.place((x, y)):
            print("Invalid input, try again: ")
            x, y = map(int, input().split())
        print(grid)
