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
    """
    Test suite for the check_for_winner() method.

    Tests cover:
    - No winner on empty or partial board
    - Horizontal win (4 in a row)
    - Vertical win (4 in a column)
    - Positive diagonal (top-left to bottom-right)
    - Negative diagonal (bottom-left to top-right)
    - Only the color that has 4 in a row wins; the other does not
    """

    def setUp(self):
        """Create a fresh GameBoard before each test."""
        self.board = GameBoard()

    def test_no_winner_on_empty_board(self):
        """Neither color should win on an empty board."""
        self.assertFalse(self.board.check_for_winner("red"))
        self.assertFalse(self.board.check_for_winner("yellow"))
        self.board.print_board()

    def test_no_winner_with_few_coins(self):
        """Three in a row should not count as a win."""
        for col in range(3):
            self.board.add_coin("red", col)
        self.assertFalse(self.board.check_for_winner("red"))
        self.assertFalse(self.board.check_for_winner("yellow"))
        self.board.print_board()

    def test_horizontal_win_red(self):
        """Four red coins in a horizontal row should make red the winner."""
        for col in range(4):
            self.board.add_coin("red", col)
        self.assertTrue(self.board.check_for_winner("red"))
        self.assertFalse(self.board.check_for_winner("yellow"))
        self.board.print_board()

    def test_horizontal_win_yellow(self):
        """Four yellow coins in a horizontal row should make yellow the winner."""
        for col in range(2, 6):
            self.board.add_coin("yellow", col)
        self.assertTrue(self.board.check_for_winner("yellow"))
        self.assertFalse(self.board.check_for_winner("red"))
        self.board.print_board()

    def test_vertical_win_red(self):
        """Four red coins in one column should make red the winner."""
        for _ in range(4):
            self.board.add_coin("red", 3)
        self.assertTrue(self.board.check_for_winner("red"))
        self.assertFalse(self.board.check_for_winner("yellow"))
        self.board.print_board()

    def test_vertical_win_yellow(self):
        """Four yellow coins in one column should make yellow the winner."""
        for _ in range(4):
            self.board.add_coin("yellow", 0)
        self.assertTrue(self.board.check_for_winner("yellow"))
        self.assertFalse(self.board.check_for_winner("red"))
        self.board.print_board()

    def test_positive_diagonal_win_red(self):
        """Four red coins on a positive diagonal (bottom-left to middle-middle) should make red the winner."""
        # Build diagonal at positions (0,0), (1,1), (2,2), (3,3) by filling below with other color
        self.board._board[0][0] = COIN_RED
        self.board._board[1][1] = COIN_RED
        self.board._board[2][2] = COIN_RED
        self.board._board[3][3] = COIN_RED
        self.assertTrue(self.board.check_for_winner("red"))
        self.assertFalse(self.board.check_for_winner("yellow"))
        self.board.print_board()
    
    def test_positive_diagonal_win_yellow(self):
        """Four yellow coins on a positive diagonal (top-middle to middle-right) should make yellow the winner."""
        # Build diagonal at positions (2,3), (3,4), (4,5), (5,6) by filling below with other color
        self.board._board[2][3] = COIN_YELLOW
        self.board._board[3][4] = COIN_YELLOW
        self.board._board[4][5] = COIN_YELLOW
        self.board._board[5][6] = COIN_YELLOW
        self.assertTrue(self.board.check_for_winner("yellow"))
        self.assertFalse(self.board.check_for_winner("red"))
        self.board.print_board()

    def test_negative_diagonal_win_red(self):
        """Four red coins on a positive diagonal (bottom-left to middle-middle) should make red the winner."""
        # Build diagonal at positions (2,3), (3,2), (4,1), (5,0) by filling below with other color
        self.board._board[2][3] = COIN_RED
        self.board._board[3][2] = COIN_RED
        self.board._board[4][1] = COIN_RED
        self.board._board[5][0] = COIN_RED
        self.assertTrue(self.board.check_for_winner("red"))
        self.assertFalse(self.board.check_for_winner("yellow"))
        self.board.print_board()

    def test_negative_diagonal_win_yellow(self):
        """Four yellow coins on a negative diagonal (bottom-left to middle-middle) should make yellow the winner."""
        # Build diagonal at (5,0), (4,1), (3,2), (2,3)
        self.board._board[3][3] = COIN_YELLOW
        self.board._board[2][4] = COIN_YELLOW
        self.board._board[1][5] = COIN_YELLOW
        self.board._board[0][6] = COIN_YELLOW
        self.assertTrue(self.board.check_for_winner("yellow"))
        self.assertFalse(self.board.check_for_winner("red"))
        self.board.print_board()


class TestDrawCheck(unittest.TestCase):
    """
    Test suite for the check_for_draw() method.

    Tests cover:
    - Empty board is not a draw
    - Partially filled board is not a draw
    - Full board is a draw
    """

    def setUp(self):
        """Create a fresh GameBoard before each test."""
        self.board = GameBoard()

    def test_empty_board_is_not_draw(self):
        """An empty board should not be considered a draw."""
        self.assertFalse(self.board.check_for_draw())
        self.board.print_board()

    def test_partially_filled_board_is_not_draw(self):
        """A board with some coins but free columns should not be a draw."""
        for col in range(4):
            for _ in range(6):
                self.board.add_coin("red" if col % 2 == 0 else "yellow", col)
        self.assertFalse(self.board.check_for_draw())
        self.board.print_board()

    def test_full_board_is_draw(self):
        """When every column is full (top row has no empty cell), the game is a draw."""
        for col in range(7):
            for _ in range(6):
                self.board.add_coin("red" if col % 2 == 0 else "yellow", col)
        self.assertTrue(self.board.check_for_draw())
        self.board.print_board()

if __name__ == "__main__":
    unittest.main()
