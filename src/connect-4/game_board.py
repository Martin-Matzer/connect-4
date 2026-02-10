

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

    def add_coin(self, color: str, column: int) -> bool:
        """
        Method for adding a new coin into the game board.
        This method takes two parameter and returns True if the coin can be added to the given column of the board.
        It will return False f the coin cannot be added anymore to the given column because it is full.
        :param color: str - "red" or "yellow" - color of the coin which should be added to the board
        :param column: int - number of the column where the coin should be added
        :return: bool - True for success and False if coin cannot be added anymore
        """

        # Check if the given column is already full
        if self._board[0][column - 1] != "":
            return False
        else:
            # Add coin to the lowest possible row
            for i in range(self._rows - 1, -1, -1):
                if self._board[i][column - 1] == "":
                    if color == "red":
                        self._board[i][column - 1] = "🔴"
                        return True
                    else:
                        self._board[i][column - 1] = "🟡"
                        return True

    def check_for_winner(self) -> str:
        pass

    def check_for_draw(self) -> bool:
        """

        :return:
        """

        draw = True

        for i in range(0, self._columns):
            if self._board[0][i] == "":
                draw = False

        return draw


    def reset_board(self):
        """
        Method for removing all coins from the game board for starting a new game.
        :return:
        """

        self._board = [
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
        ]


if __name__ == "__main__":
    board = GameBoard()
    board.print_board()