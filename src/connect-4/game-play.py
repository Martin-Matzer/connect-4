#File to execute the game logic itself
from GameSetup import GameSetup
from ClassesPlayers import HumanPlayer, Bot
from game_board import GameBoard

print("Welcome to Connect-4!")

#Outline logic for game

#Create setup
setup = GameSetup()
#Select number of players
num_players = setup.choose_players()
#Create player objects
players = setup.create_players(num_players)
#Select starting player
setup.pick_starting_player(players)
#Create empty board
board = GameBoard()

#Play game until one winner or draw
#Loop needed with methods
#play_turn (players)
#add_coin (board)
#print_board 
#check_for_winner and check_for_draw

#If winner is existing: announce winner
#In case of draw: announce draw

#Empty board and possibly restart game

