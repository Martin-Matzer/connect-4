import unittest

from connect4 import GameBoard


class TestAddCoin(unittest.TestCase):
    """
    Test suite for the add_coin() method.

    Tests cover:
    - Valid moves in empty columns
    - Stacking coins in the same column
    - Full column rejection
    - Both player colors (red and yellow)
    - All column positions (0-6)
    - Invalid column number rejection
    """

    # Standard cases
    def test_add_coin_to_empty_column_red(self):
        """
        Test adding a red coin to an empty column.
        """
        board = GameBoard()
        assert board.add_coin("red", 3)
        board.print_board()
        assert board._board[5][3] == "🔴"

    def test_add_coin_to_empty_column_red(self):
        """
        Test adding a yellow coin to an empty column.
        """
        board = GameBoard()
        assert board.add_coin("yellow", 5)
        board.print_board()
        assert board._board[5][5] == "🟡"

    def test_add_6_coins_to_one_column_red(self):
        """
        Test adding a 6 red coins to one column.
        """
        board = GameBoard()

        for _ in range(6):
            assert board.add_coin("red", 0)

        for i in range(6):
            assert board._board[i][3] == "🔴"

        board.print_board()

    def test_add_6_coins_to_one_column_yellow(self):
        """
        Test adding a 6 yellow coins to one column.
        """
        board = GameBoard()

        for _ in range(6):
            assert board.add_coin("yellow", 6)

        for i in range(6):
            assert board._board[i][3] == "🟡"

        board.print_board()

    # Edge cases

    def test_add_coin_to_full_column_red(self):
        """
        Test adding red coin to already full column.
        """
        board = GameBoard()

        for _ in range(6):
            assert board.add_coin("red", 4)

        for i in range(6):
            assert board._board[i][3] == "🔴"

        assert not board.add_coin("red", 4)

        board.print_board()
    def test_add_coin_to_full_column_yellow(self):
        """
        Test adding yellow coin to already full column.
        """
        board = GameBoard()

        for _ in range(6):
            assert board.add_coin("yellow", 6)

        for i in range(6):
            assert board._board[i][3] == "🟡"

        assert not board.add_coin("yellow", 6)

        board.print_board()


class TestWinCheck(unittest.TestCase):
    pass


class TestDrawCheck(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
