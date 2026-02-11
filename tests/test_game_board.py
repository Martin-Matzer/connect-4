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
    """

    def test_add_coin_to_empty_column_red(self):
        """
        Test adding a red coin to an empty column.

        The coin should be placed at the bottom row (row 5) and
        the method should return True.
        """
        board = GameBoard()
        result = board.add_coin("red", 3)
        board.print_board()

        assert result == True
        assert board._board[5][3] == "🔴"


class TestWinCheck(unittest.TestCase):
    pass


class TestDrawCheck(unittest.TestCase):
    pass