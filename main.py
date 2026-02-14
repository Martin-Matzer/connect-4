#File to execute the game logic itself
from connect4 import GameSetup, GameBoard

print("Welcome to Connect-4!")
print("""
    Rules:
    Players take turns dropping one disc into any column.
    The disc falls to the lowest empty space in that column.
    The goal is to connect four of your discs in a row (horizontal, vertical, or diagonal).
    The first player to connect four wins.
    If the grid fills and no one connects four, the game is a draw.
    -------------
    To surrender the game please enter "I surrender!" on your turn.
    """)
print("Let's begin! \n\n")


#Outline logic for game

#Create setup
setup = GameSetup()

#Create empty board
board = GameBoard()

#Select number of players
num_players = setup.choose_players()

#Create player objects
players = setup.create_players(num_players)

while True:
    #Select starting player
    starter = setup.pick_starting_player(players)

    #Assigning player1 and player2
    player1 = starter
    player2 = players[0] if starter is players[1] else players[1]

    #Print empty board
    board.print_board()

    #Play game until one winner or draw 
    game_over = False
    while not game_over:

        move = player1.play_turn(board)
        if move is None:
            print(f"{player2.name} has won the game! {player1.name} surrendered.")
            game_over = True
            break

        # Keep asking until the coin is placed (full or invalid column)
        while True:
            result = board.add_coin(player1.color, move)
            if result is True:
                break
            print(result if type(result) == str else "The last turn was not valid. Please enter a valid column.")
            move = player1.play_turn(board)
            if move is None:
                print(f"{player2.name} has won the game! {player1.name} surrendered.")
                game_over = True
                break
        if move is None:
            break

        board.print_board()

        if board.check_for_winner(player1.color):
            print(f"{player1.name} has won the game!")
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

        # Keep asking until the coin is placed (full or invalid column)
        while True:
            result = board.add_coin(player2.color, move)
            if result is True:
                break
            print(result if type(result) == str else "The last turn was not valid. Please enter a valid column.")
            move = player2.play_turn(board)
            if move is None:
                print(f"{player1.name} has won the game! {player2.name} surrendered.")
                game_over = True
                break
        if move is None:
            break

        board.print_board()

        if board.check_for_winner(player2.color):
            print(f"{player2.name} has won the game!")
            game_over = True
            break

        elif board.check_for_draw():
            print("Game has ended with a draw.")
            game_over = True
            break
    #End game

    #Clear board
    board.reset_board()

    #Option to play again
    if not setup.choose_to_play_again():
        print("Thanks for playing!")
        break    