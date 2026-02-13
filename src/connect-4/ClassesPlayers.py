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
    def play_turn(self):
        pass


class HumanPlayer(Players):

    def play_turn(self):
        column = int(input(f"Player {self.player_no}, choose column: "))
        print(f"Player {self.player_no} plays column {column}")
        return column


    def surrender_game(self):
        print(f"Player {self.player_no} surrendered!")


class Bot(Players):

    def play_turn(self):
        column = random.randint(0, 6)
        print(f"Hansi plays column {column}")
        return column



if __name__ == '__main__':
    p1 = HumanPlayer()
    p2 = HumanPlayer()