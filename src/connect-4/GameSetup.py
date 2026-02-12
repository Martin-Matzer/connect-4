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
    def start_computer_opponent(self):
        pass

    # Selects starting player
    def pick_starting_player(self):
        pass
