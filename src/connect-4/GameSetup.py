import random
from ClassesPlayers import HumanPlayer, Bot

# Class for game setup
# Selection for number of players and starting player
class GameSetup:

    #Defines number of human players and if bot is needed
    def choose_players(self) -> int:
        while True:
            print("Choose number of players:")
            print("1 - single player")
            print("2 - two player")
            selection = input("> ").strip()
            if selection in ("1", "2"):
                return int(selection)
            print("Invalid input. Please enter 1 or 2.\n")
    
    # Initializes bot
    def create_players(self, num_players):
        players = []
        for i in range(num_players):
            player = HumanPlayer(f"p{i+1}")
            players.append(player)
        if num_players == 1:
            players.append(Bot("p2"))
        return players

    # Selects starting player
    def pick_starting_player(self, players:list):
        starter = random.choice(players)
        print(f"{starter.color} beginnt!")
        starter.onturn = True

#Tests for created methods
#Will be removed after final testing
setup = GameSetup()
num_players = setup.choose_players()
print(num_players)
players = setup.create_players(num_players)
print(players)
print(players[0], players[1])

setup.pick_starting_player(players)