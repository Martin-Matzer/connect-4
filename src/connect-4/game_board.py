

class GameBoard:

    rows = 6
    columns = 7
    possibleColumns = ["1", "2", "3", "4", "5", "6", "7"]
    board = [
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
    ]

    def _print_board_header(self):
        print("\nWelcome to Connect 4 game!")

    def _print_board_footer(self):
        #print("\nIn which column would you like to place your next chip?")
        pass

    def print_board(self):
        self._print_board_header()
        print("\n     1    2    3    4    5    6    7   ", end="")

        for x in range(self.rows):
            print("\n   +----+----+----+----+----+----+----+")
            print(x, " |", end="")

            for y in range(self.columns):
                if self.board[x][y] == "🟡":
                    print("", self.board[x][y], end=" |")
                elif self.board[x][y] == "🔴":
                    print("", self.board[x][y], end=" |")
                else:
                    print(" ", self.board[x][y], end="  |")

        print("\n   +----+----+----+----+----+----+----+")
        self._print_board_footer()

if __name__ == "__main__":
    board = GameBoard()
    board.print_board()