from abc import ABC, abstractmethod
import random

#Abstract Player class to add abstract methods
class Player(ABC):

    _next_player_number = 1

    # Player No cannot be assigned manually - done by system
    def __init__(self, name):
        self._player_number = Player._next_player_number
        Player._next_player_number += 1
        self._name = name
        if self._player_number == 1:
            self._color = "red"
        else:
            self._color = "yellow"

    def __str__(self):
        return f"Player{self._player_number}: {self.color}"

    #Getter for protected attributes
    @property
    def player_number(self):
        return self._player_number
    
    @property
    def name(self):
        return self._name
    
    @property
    def color(self):
        return self._color

    @abstractmethod
    def play_turn(self, board):
        pass




class HumanPlayer(Player):

    def surrender(self):
        print(f"Player {self.player_number} surrendered!")

    def play_turn(self, board) -> int:
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

    def play_turn(self, board) -> int:
        column = random.randint(0, 6)
        print(f"{self.name} plays column {column}")
        return column



class SmartBot(Player):

    def play_turn(self, board) -> int:
        valid_columns = self._valid_columns(board)

        # 1) Check for win 
        for column in valid_columns:
            if self._would_win(board, self.color, column):
                print(f"{self.name} plays column {column}")
                return column

        # 2) Check for blocking player
        opp_color = "yellow" if self.color == "red" else "red"
        for column in valid_columns:
            if self._would_win(board, opp_color, column):
                print(f"{self.name} plays column {column}")
                return column

        # 3) Prioritize playing middle columns
        preferred = [3, 2, 4, 1, 5, 0, 6]
        for column in preferred:
            if column in valid_columns:
                print(f"{self.name} plays column {column}")
                return column

        # Fallback 
        column = random.choice(valid_columns)
        print(f"{self.name} plays column {column}")
        return column


    # Supporting method for play_turn()
    def _valid_columns(self, board):
        # checks game board for open columns
        return [c for c in range(7) if board._board[0][c] == ""]


    # Supporting method for play_turn()
    def _would_win(self, board, color, column):
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
