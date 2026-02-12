from abc import ABC, abstractmethod
import random

#Abstract Player class to add abstract methods
class Players(ABC):

    _next_player_no = 1

    # Player No cannot be assigned manually - done by system
    def __init__(self):
        self.__player_no = Players._next_player_no
        Players._next_player_no += 1
        self.onturn = False
        self.total_wins = 0
        self.total_turns = 0
        self.current_turns = 0
        #How should playing colors be assigned? Bug with more than 2 objects expected
        if self.__player_no == 1:
            self.color = "red"
        else:
            self.color = "yellow"

    def __str__(self):
        return f"Player{self.player_no} : {self.color}"

    @property
    def player_no(self):
        return self.__player_no


    @abstractmethod
    def play_turn(self):
        pass

    @abstractmethod
    def surrender_game(self):
        pass


class HumanPlayer(Players):

    def play_turn(self):
        column = input(f"Player {self.player_no}, choose column: ")
        print(f"Player {self.player_no} plays column {column}")
        self.current_turns += 1
        self.total_turns += 1


    def surrender_game(self):
        print(f"Player {self.player_no} surrendered!")
        #To Do
        #how to access total wins of other player?


class Bot(Players):

    def play_turn(self):
        column = random.randint(0, 6)
        print(f"Hansi plays column {column}")
        self.current_turns += 1
        self.total_turns += 1

    def surrender_game(self):
        print("Hansi never  surrenders 😎")
        #Method even needed?


"""
if __name__ == '__main__':
    p1 = HumanPlayer()
    print(p1)
    p2 = HumanPlayer()
    print(p2)
    p3 = Bot()
    print(p3)
    p3.play_turn()

"""