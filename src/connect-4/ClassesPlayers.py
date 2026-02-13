from abc import ABC, abstractmethod
import random

#Abstract Player class to add abstract methods
class Players(ABC):

    _next_player_no = 1

    # Player No cannot be assigned manually - done by system
    def __init__(self, _name):
        self._player_no = Players._next_player_no
        Players._next_player_no += 1
        self._name = _name
        self.onturn = False
        #How should playing colors be assigned? Bug with more than 2 objects expected
        if self._player_no == 1:
            self._color = "red"
        else:
            self._color = "yellow"

    def __str__(self):
        return f"Player{self.player_no} : {self.color}"

    #Getter for protected attributes
    @property
    def player_no(self):
        return self._player_no
    
    @property
    def name(self):
        return self._name
    
    @property
    def color(self):
        return self._color

    @abstractmethod
    def play_turn(self, board):
        pass




class HumanPlayer(Players):

    def play_turn(self, board):
        column = int(input(f"Player {self.player_no}, choose column: "))
        print(f"Player {self.player_no} plays column {column}")
        return column


    def surrender_game(self):
        print(f"Player {self.player_no} surrendered!")




class Bot(Players):

    def play_turn(self, board):
        column = random.randint(0, 6)
        print(f"Hansi plays column {column}")
        return column



class SmartBot(Players):

    def play_turn(self, board):
        valid_cols = self._valid_columns(board)

        # 1) Check for win 
        for column in valid_cols:
            if self._would_win(board, self.color, column):
                print(f"{self.name} plays column {column}")
                return column

        # 2) Check for blocking player
        opp_color = "yellow" if self.color == "red" else "red"
        for column in valid_cols:
            if self._would_win(board, opp_color, column):
                print(f"{self.name} plays column {column}")
                return column

        # 3) Prioritize playing middle columns
        preferred = [3, 2, 4, 1, 5, 0, 6]
        for column in preferred:
            if column in valid_cols:
                print(f"{self.name} plays column {column}")
                return column

        # Fallback 
        column = random.choice(valid_cols)
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
    p1 = HumanPlayer()
    p2 = HumanPlayer()