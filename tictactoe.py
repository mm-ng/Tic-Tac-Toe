from sys import stdin

NROWS = 3
NCOLS = 3

########## HELPER FUNCTIONS ##########

# Prints the game board in a pretty format.
def print_board(board):
    for r in range(NROWS):
        for c in range(NCOLS):
            if c == NCOLS - 1:
                print(board[r][c] + " ")
            else:
                print(board[r][c] + " ", end="")
    print("\n")


# Given a coodinate and a board, determines if move is valid.
# Prints the respective error messages.
def check_valid_move(board, xcoord, ycoord):
    # Invalid coordinate range.
    if not 0 <= xcoord - 1 < NROWS or not 0 <= ycoord - 1 < NCOLS:
        print("\nInvalid coordinate range. Please enter numbers between 1 and 3.\n")
        return False
    # Board is already occupied at given coordinate.
    elif board[xcoord-1][ycoord-1] != '.':
        print("\nOh no, a piece is already at this place! Try again...\n")
        return False
    else:
        return True


# Checks whether a player has won yet. The game progresses if neither player has won.
def has_player_won(board):
    # Check rows for three in a row.
    for r in board:
        if r[0] != '.' and (r[0] == r[1] == r[2]):
            return True

    # Check cols for three in a row.
    for c in range(NROWS):
        if board[0][c] != '.' and board[0][c] == board[1][c] == board[2][c]:
            return True

    # Check diagonals for three in a row.
    if board[0][0] != '.' and board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[2][0] != '.' and board[2][0] == board[1][1] == board[0][2]:
        return True
    
    # No winning combination found, game progresses.
    return False


def is_board_full(board):
    for r in range(NROWS):
        for c in range(NCOLS):
            if board[r][c] == '.':
                return False
    
    return True


########## MAIN GAME LOOP ##########

game_in_progress = True
board = [['.'] * NCOLS for i in range(NROWS)]
player_turn = '1'

print("Welcome to Tic Tac Toe!\n")
print("Here's the current board:\n")
print_board(board)


while (game_in_progress):
    player_input = ""

    # Prompt current player to make a move.
    if player_turn == "1":
        player_input = input("Player 1 enter a coord x,y to place your X or enter 'q' to give up: ")
    elif player_turn == "2":
        player_input = input("Player 2 enter a coord x,y to place your O or enter 'q' to give up: ")

    # Parse player's move.
    if player_input == 'q':
        print("Quitting the game...\n")
        game_in_progress = False
        break
    else:
        # If player didn't quit, try to extract coordinates.
        try:
            x, y = player_input.split(',')
            x, y = int(x), int(y)

            # Makes the move if proposed move is valid.
            if check_valid_move(board, x, y):
                board[x-1][y-1] = 'X' if player_turn == '1' else 'O'
            
                if has_player_won(board):
                    print("\nMove accepted, well done you've won the game!\n")
                    print_board(board)
                    break
                else:
                    print("\nMove accepted, here's the current board:\n")
                    print_board(board)
            else:
                # The move at the given coordinate was invalid, prompts player to try again.
                continue
        except:
            # The move format was invalid, prompts player to try again.
            print("\nPlease enter a valid move.\n")
            continue

    # Switches the turn to the other player.
    player_turn = '1' if player_turn == '2' else '2'

    if is_board_full(board):
        print("Game over, it's a draw.\n")
        game_in_progress = False
