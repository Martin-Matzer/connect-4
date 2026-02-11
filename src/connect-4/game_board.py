

class GameBoard:
    """
    This class is responsible to hold the data regarding the game board and provide the necessary methods for board handling.

    While initialising the class, an empty game board will be created and some constants regarding the row and column count are defined.
    The current state of the board during the game will be stored in the class.
    It provides also all necessary methods for printing the board to the command line, adding a new coin to the board + checking if the turn is valid,
    checking for winner or draw and resetting the board state if a new game is started.
    """

    def __init__(self):
        """
        Initialises the class GameBoard, defines some constants and creates an empty game board.
        """
        self._ROW_COUNT = 6
        self._COLUMN_COUNT = 7
        self._possibleColumns = ["0", "1", "2", "3", "4", "5", "6"]
        self._board = [
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
        ]

    def print_board(self):
        """
        Method for printing the current state of the game board which is stored in the protected attribut _board to the command line.
        """

        print("\n     0    1    2    3    4    5    6   ", end="")

        for x in range(self._ROW_COUNT):
            print("\n   +----+----+----+----+----+----+----+")
            print(x, " |", end="")

            for y in range(self._COLUMN_COUNT):
                if self._board[x][y] == "🟡":
                    print("", self._board[x][y], end=" |")
                elif self._board[x][y] == "🔴":
                    print("", self._board[x][y], end=" |")
                else:
                    print(" ", self._board[x][y], end="  |")

        print("\n   +----+----+----+----+----+----+----+")

    def add_coin(self, color: str, column: int) -> bool:
        """
        Method for adding a new coin into the game board if the turn is valid.

        This method takes two parameters (color and column) and returns True if the coin can be added to the given column of the board.
        It will return False f the coin cannot be added anymore to the given column because it is full.

        Parameters
        ----------
        :param color: str - "red" or "yellow"
            Color of the coin which should be added to the board
        :param column: int
            Number of the column where the coin should be added

        Returns
        -------
        :return: bool
            True for a valid turn and successful adding to game board.
            False for a not valid turn when coin cannot be added to the given column.
        """

        # Check if the given column is already full
        if self._board[0][column] != "":
            return False
        else:
            # Add coin to the lowest possible row
            for i in range(self._ROW_COUNT - 1, -1, -1):
                if self._board[i][column] == "":
                    if color == "red":
                        self._board[i][column] = "🔴"
                        return True
                    else:
                        self._board[i][column] = "🟡"
                        return True

    def _count_direction(self, row: int, column: int, delta_row: int, delta_column: int, color: str):
        """


        Parameters
        ----------
        :param row:
        :param column:
        :param delta_row:
        :param delta_column:
        :param color:

        Returns
        -------
        :return:
        """

        pass

    def check_for_winner(self, coin) -> bool:
        """
        Check the board for winner with the provided coin.

        Method will return True if the board already has 4 piece of the provided coin in row, column or diagonal.

        Parameters
        ----------
        :param coin: str
            Type of coin for which the win check is executed.

        Returns
        -------
        :return: bool
            True if the provided coin has won.
            False if the provided coin has not won yet.
        """

        # check for horizontal win
        for r in range(self._ROW_COUNT):
            for c in range(self._COLUMN_COUNT - 3):
                if self._board[r][c] == coin and self._board[r][c + 1] == coin and self._board[r][c + 2] == coin and self._board[r][c + 3] == coin:
                    return True


        # check for vertical win
        for r in range(self._ROW_COUNT - 3):
            for c in range(self._COLUMN_COUNT):
                if self._board[r][c] == coin and self._board[r + 1][c] == coin and self._board[r + 2][c] == coin and self._board[r + 3][c] == coin:
                    return True

        # check for positive diagonal win
        for r in range(self._ROW_COUNT - 3):
            for c in range(self._COLUMN_COUNT - 3):
                if self._board[r][c] == coin and self._board[r + 1][c + 1] == coin and self._board[r + 2][c + 2] == coin and self._board[r + 3][c + 3] == coin:
                    return True

        # check for negative diagonal win:
        for r in range(3, self._ROW_COUNT):
            for c in range(self._COLUMN_COUNT - 3):
                if self._board[r][c] == coin and self._board[r - 1][c + 1] == coin and self._board[r - 2][c - 2] == coin and self._board[r - 3][c - 3] == coin:
                    return True

    def check_for_draw(self) -> bool:
        """
        Method to check if the game board is already full. This would mean that the game ended with draw.

        Returns
        -------
        :return: bool - True if draw otherwise False
        """

        draw = True

        for i in range(0, self._COLUMN_COUNT):
            if self._board[0][i] == "":
                draw = False

        return draw


    def reset_board(self):
        """
        Method for removing all coins from the game board for starting a new game.
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