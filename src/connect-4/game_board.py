

class GameBoard:

    def __init__(self):
        self._rows = 6
        self._columns = 7
        self._possibleColumns = possibleColumns = ["1", "2", "3", "4", "5", "6", "7"]
        self._board = [
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

        for x in range(self._rows):
            print("\n   +----+----+----+----+----+----+----+")
            print(x, " |", end="")

            for y in range(self._columns):
                if self._board[x][y] == "🟡":
                    print("", self._board[x][y], end=" |")
                elif self._board[x][y] == "🔴":
                    print("", self._board[x][y], end=" |")
                else:
                    print(" ", self._board[x][y], end="  |")

        print("\n   +----+----+----+----+----+----+----+")
        self._print_board_footer()


    def reset_board(self):
        pass

    def check_turn(self, column: int):
        pass

    def check_for_winner(self):
        pass

    def check_for_draw(self):
        pass


if __name__ == "__main__":
    board = GameBoard()
    board.print_board()