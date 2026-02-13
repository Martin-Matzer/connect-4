import random
from ClassesPlayers import HumanPlayer, Bot, SmartBot

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

    #Method to select difficulty of bot
    def choose_bot_difficulty(self) -> int:
        while True:
            print("Choose bot difficulty:")
            print("0 - play against Hansi")
            print("1 - play against SuperHansi")
            selection = input("> ").strip()
            if selection in ("0", "1"):
                return int(selection)
            print("Invalid input. Please enter 0 or 1.\n")
    
    # Initializes player(s) and bot (if needed)
    def create_players(self, num_players):
        players = []
        for i in range(num_players):
            player = HumanPlayer(f"Player{i+1}")
            players.append(player)
        if num_players == 1:
            difficulty = self.choose_bot_difficulty()
            if difficulty == 0:
                players.append(Bot("Hansi"))
            else:
                players.append(SmartBot("SuperHansi"))
        return players

    # Selects starting player
    def pick_starting_player(self, players:list):
        starter = random.choice(players)
        print(f"{starter.name} beginns!")
        starter.onturn = True

    # Method to trigger play again
    def play_again(self):
        while True:
            play_again = input("Play again? Please enter yes or no:").lower()
            if play_again == "yes":
                return True
            elif play_again == "no":
                return False
            else:
                print("Invalid input. Please enter yes or no")


if __name__ == '__main__':
    setup = GameSetup()
    num_players = setup.choose_players()
    print(num_players)
    players = setup.create_players(num_players)
    print(players)
    print(players[0], players[1])
    setup.pick_starting_player(players)
    print(setup.play_again())
