"""Game setup helpers for a Connect Four style game.

This module contains logic for setting up a game session through terminal
interaction: selecting the number of players, selecting bot difficulty, creating
player objects, and choosing a starting player.
"""

import random
from players import HumanPlayer, Bot, SmartBot, Player


class GameSetup:
    """Handle interactive game setup.

    Responsibilities
    ----------------
    - Ask whether the game is single-player or two-player.
    - Ask bot difficulty (for single-player games).
    - Create player objects based on the chosen configuration.
    - Randomly select the starting player.
    - Ask whether to play another game after finishing.

    Notes
    -----
    This class assumes a terminal/CLI environment and uses ``input()`` and
    ``print()`` for interaction.
    """

    
    def choose_players(self) -> int:
        """Ask the user for the number of human players.

        Returns
        -------
        int
            Number of human players (1 or 2).
        """
        while True:
            print("Choose number of players:")
            print("1 - single player")
            print("2 - two player")
            selection = input("> ").strip()
            if selection in ("1", "2"):
                return int(selection)
            print("Invalid input. Please enter 1 or 2.\n")


    def choose_bot_difficulty(self) -> int:
        """Ask the user to choose the bot difficulty.

        Returns
        -------
        int
            Difficulty level:
            - 0: simple bot (Bot)
            - 1: smart bot (SmartBot)
        """
        while True:
            print("\nChoose bot difficulty:")
            print("0 - play against Hansi")
            print("1 - play against SuperHansi")
            selection = input("> ").strip()
            if selection in ("0", "1"):
                return int(selection)
            print("Invalid input. Please enter 0 or 1.\n")
    
    
    def create_players(self, num_players: int) -> list[Player]:
        """Create player and bot instances based on setup choices.

        Parameters
        ----------
        num_players : int
            Number of human players (1 or 2). If 1, a bot will be added as the
            second player.

        Returns
        -------
        list[Player]
            List of player objects (HumanPlayer plus optional Bot/SmartBot).
        """
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

    
    def pick_starting_player(self, players: list[Player]) -> Player:
        """Randomly select which player begins.

        Parameters
        ----------
        players : list[Player]
            List of player objects to choose from.

        Returns
        -------
        Player
            The selected starting player instance.
        """
        starter = random.choice(players)
        print(f"\n{starter.name} begins!")
        return starter
        

    
    def choose_to_play_again(self) -> bool:
        """Ask the user whether to start another game.

        Returns
        -------
        bool
            True if the user wants to play again, otherwise False.
        """
        while True:
            play_again = input("Play again? Please enter yes or no:").strip().lower()
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
    print(setup.choose_to_play_again())
