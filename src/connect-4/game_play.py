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
player1 = players[0]
player2 = players[1]

#Select starting player
setup.pick_starting_player(players)
#Create empty board
board = GameBoard()

#Print empty board
board.print_board()

#Play game until one winner or draw
#Loop needed with methods
#play_turn (players)
#add_coin (board)
#print_board 
#check_for_winner and check_for_draw

game_over = False

while not game_over:

    move = player1.play_turn(board)
    if move is None:
        print(f"{player2.name} has won the game! {player1.name} surrendered.")
        game_over = True
        break

    while not board.add_coin(player1.color, move):
        print("The last turn was not valid. Please enter a valid column.")

    board.print_board()

    if board.check_for_winner(player1.color):
        print("Player1 has won the game!")
        game_over = True
        break

    elif board.check_for_draw():
        print("Game has ended with a draw.")
        game_over = True
        break


    move = player2.play_turn(board)
    if move is None:
        print(f"{player1.name} has won the game! {player2.name} surrendered.")
        game_over = True
        break
    

    while not board.add_coin(player2.color, move):
        print("The last turn was not valid. Please enter a valid column.")

        if board.check_for_winner(player1.color):
            print("Player1 has won the game!")
            game_over = True
            break

        elif board.check_for_draw():
            print("Game has ended with a draw.")
            game_over = True
            break

    board.print_board()








#If winner is existing: announce winner
#In case of draw: announce draw

#Empty board and possibly restart game

