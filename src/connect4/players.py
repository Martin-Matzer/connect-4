"""Player classes for a Connect Four style game.

This module defines the abstract player interface and concrete implementations
for human players and computer-controlled bots.

Classes
-------
Player
    Abstract base class defining the player interface.
HumanPlayer
    Human-controlled player that selects a move via user input.
Bot
    Simple bot that chooses a random valid column.
SmartBot
    Bot that tries to win, block the opponent, and prefers central columns.
"""

from abc import ABC, abstractmethod
import random
from .game_board import GameBoard



class Player(ABC):
    """Abstract base class for all player types.

    Each player has a unique automatically assigned player number, a name,
    and a playing color.

    Attributes
    ----------
    _next_player_number : int
        Class-level counter used to assign unique player numbers.

    Notes
    -----
    The color assignment is currently based on the order of creation:
    player 1 gets "red", all others get "yellow".
    """

    _next_player_number = 1

    
    def __init__(self, name: str):
        """Initialize a player.

        Parameters
        ----------
        name : str
            Display name of the player.
        """
        self._player_number = Player._next_player_number
        Player._next_player_number += 1
        self._name = name
        if self._player_number == 1:
            self._color = "red"
        else:
            self._color = "yellow"

    def __str__(self) -> str:
        """Return a readable string representation of the player.

        Returns
        -------
        str
            Player summary including number and color.
        """
        return f"Player{self._player_number}: {self.color}"

   
    @property
    def player_number(self) -> int:
        """int: Unique player number assigned automatically."""
        return self._player_number
    
    @property
    def name(self) -> str:
        """str: Player display name."""
        return self._name
    
    @property
    def color(self) -> str:
        """str: Player color identifier (e.g., 'red' or 'yellow')."""
        return self._color

    @abstractmethod
    def play_turn(self, board: GameBoard):
        """Choose a column to play for the current turn.

        Parameters
        ----------
        board : GameBoard
            Game board instance used to evaluate valid moves and game state.

        Returns
        -------
        int or None
            The chosen column index (0-6). Returns None if the player forfeits.
        """
        pass




class HumanPlayer(Player):
    """Human-controlled player.

    The human player chooses a column through terminal input. A special input
    can be used to surrender the game.
    """

    def surrender(self):
        """Surrender the game."""
        print(f"Player {self.player_number} surrendered!")


    def play_turn(self, board: GameBoard) -> int:
        """Ask the player for a column choice via input.

        Parameters
        ----------
        board : GameBoard
            Game board instance (currently not used for input validation).

        Returns
        -------
        int or None
            Selected column index (0-6) or None if the player surrenders.
        """
        while True:
            column = input(f"Player{self.player_number}, choose column: ")
            if column in ("0", "1", "2", "3", "4", "5", "6"):
                return int(column)
            elif column == "I surrender!":
                self.surrender()
                return None
            else:
                print("Invalid input. Please enter a column or surrender your soul.\n")



class Bot(Player):
    """Simple bot player that selects a random column to play."""

    def play_turn(self, board: GameBoard) -> int:
        """Choose a random column.

        Parameters
        ----------
        board : GameBoard
            Game board instance (currently not used for move validation).

        Returns
        -------
        int
            Randomly selected column index (0-6).
        """
        column = random.randint(0, 6)
        print(f"{self.name} plays column {column}")
        return column



class SmartBot(Player):
    """Bot that selects moves based on simple heuristics.

    Strategy
    --------
    1. Play a winning move if available.
    2. Block the opponent's winning move.
    3. Prefer central columns for positional advantage.
    4. Fallback to a random valid move.
    """

    def play_turn(self, board: GameBoard) -> int:
        """Select a column using the SmartBot strategy.

        Parameters
        ----------
        board : GameBoard
            Game board instance used to evaluate valid columns and winners.
            The board is expected to provide:
            - a 2D list/array attribute ``_board`` with empty slots as ""
            - a method ``check_for_winner(color: str) -> bool``

        Returns
        -------
        int
            Selected column index.
        """
        valid_columns = self._valid_columns(board)

        # Play a winning move if available.
        for column in valid_columns:
            if self._would_win(board, self.color, column):
                print(f"{self.name} plays column {column}")
                return column

        # Block the opponent's winning move.
        opponent_color = "yellow" if self.color == "red" else "red"
        for column in valid_columns:
            if self._would_win(board, opponent_color, column):
                print(f"{self.name} plays column {column}")
                return column

        # Prefer central columns for positional advantage.
        preferred = [3, 2, 4, 1, 5, 0, 6]
        for column in preferred:
            if column in valid_columns:
                print(f"{self.name} plays column {column}")
                return column

        # Fallback to a random valid move.
        column = random.choice(valid_columns)
        print(f"{self.name} plays column {column}")
        return column


    def _valid_columns(self, board: GameBoard) -> list[int]:
        """Return a list of columns that are not full.

        Parameters
        ----------
        board : GameBoard
            Game board instance exposing ``_board`` with empty slots as "".

        Returns
        -------
        list[int]
            List of valid column indices (0-6) where a piece can be dropped.
        """
        return [c for c in range(7) if board._board[0][c] == ""]


    def _would_win(self, board: GameBoard, color: str, column: int) -> bool:
        """Check whether playing in a column would result in a win.

        This method temporarily places a coin in the target position, calls
        the board's winner detection, and then undoes the move.

        Parameters
        ----------
        board : GameBoard
            Game board instance exposing ``_board`` and ``check_for_winner``.
        color : str
            Color identifier ("red" or "yellow") to test the move for.
        column : int
            Column index to test.

        Returns
        -------
        bool
            True if the move would win the game for ``color``, otherwise False.
        """
        target_row = None
        for row in range(5, -1, -1):
            if board._board[row][column] == "":
                target_row = row
                break
        if target_row is None:
            return False

        coin = "🔴" if color == "red" else "🟡"
        board._board[target_row][column] = coin
        won = board.check_for_winner(color)
        board._board[target_row][column] = ""  # undo turn
        return won



if __name__ == '__main__':
    p1 = HumanPlayer("Player1")
    p2 = HumanPlayer("Player2")
