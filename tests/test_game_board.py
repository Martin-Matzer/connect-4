import sys
import unittest

from connect4 import GameBoard


# Constants matching GameBoard
COIN_RED = "🔴"
COIN_YELLOW = "🟡"


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

    def setUp(self):
        """Create a fresh GameBoard before each test."""
        self.board = GameBoard()

    # Standard cases
    def test_add_coin_to_empty_column_red(self):
        """Adding a red coin to an empty column should succeed and place it in the bottom row."""
        self.assertTrue(self.board.add_coin("red", 3))
        self.assertEqual(self.board._board[5][3], COIN_RED)

    def test_add_coin_to_empty_column_yellow(self):
        """Adding a yellow coin to an empty column should succeed and place it in the bottom row."""
        self.assertTrue(self.board.add_coin("yellow", 5))
        self.assertEqual(self.board._board[5][5], COIN_YELLOW)

    def test_add_6_coins_to_one_column_red(self):
        """Adding 6 red coins to one column should fill the entire column."""
        for _ in range(6):
            self.assertTrue(self.board.add_coin("red", 0))
        for i in range(6):
            self.assertEqual(self.board._board[i][0], COIN_RED)

    def test_add_6_coins_to_one_column_yellow(self):
        """Adding 6 yellow coins to one column should fill the entire column."""
        for _ in range(6):
            self.assertTrue(self.board.add_coin("yellow", 6))
        for i in range(6):
            self.assertEqual(self.board._board[i][6], COIN_YELLOW)

    # Edge cases: full column
    def test_add_coin_to_full_column_red(self):
        """Adding a red coin to an already full column should return False and not change the board."""
        for _ in range(6):
            self.assertTrue(self.board.add_coin("red", 4))
        for i in range(6):
            self.assertEqual(self.board._board[i][4], COIN_RED)
        self.assertFalse(self.board.add_coin("red", 4))

    def test_add_coin_to_full_column_yellow(self):
        """Adding a yellow coin to an already full column should return False and not change the board."""
        for _ in range(6):
            self.assertTrue(self.board.add_coin("yellow", 6))
        for i in range(6):
            self.assertEqual(self.board._board[i][6], COIN_YELLOW)
        self.assertFalse(self.board.add_coin("yellow", 6))

    def test_add_coin_to_not_available_column_left_red(self):
        """Adding a red coin to an and invalid column -1, should return string "Error, invalid column!" and not change the board."""
        board_copy = self.board._board
        self.assertEqual(self.board.add_coin("red", -1), "Error, invalid column!")
        self.assertEqual(self.board._board, board_copy)

    def test_add_coin_to_not_available_column_left_yellow(self):
        """Adding a red coin to an and invalid column -1, should return string "Error, invalid column!" and not change the board."""
        board_copy = self.board._board
        self.assertEqual(self.board.add_coin("yellow", -1), "Error, invalid column!")
        self.assertEqual(self.board._board, board_copy)

    def test_add_coin_to_not_available_column_right_red(self):
        """Adding a red coin to an and invalid column 7, should return string "Error, invalid column!" and not change the board."""
        board_copy = self.board._board
        self.assertEqual(self.board.add_coin("red", 7), "Error, invalid column!")
        self.assertEqual(self.board._board, board_copy)

    def test_add_coin_to_not_available_column_right_yellow(self):
        """Adding a yellow coin to an and invalid column 7, should return string "Error, invalid column!" and not change the board."""
        board_copy = self.board._board
        self.assertEqual(self.board.add_coin("yellow", 7), "Error, invalid column!")
        self.assertEqual(self.board._board, board_copy)

class TestWinCheck(unittest.TestCase):
    pass


class TestDrawCheck(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
