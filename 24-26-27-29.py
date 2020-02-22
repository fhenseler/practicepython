# Exercises 24, 26, 27 and 29

# Tic Tac Toe Game
# Ask the user what size game board they want to draw, 
# and draw it for them to the screen using Python’s print statement.

# Given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, 
# and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, 
# a column, or a diagonal. Don’t worry about the case where TWO people have won - assume 
# that in every board there will only be one winner.

# The next logical step is to deal with handling user input. When a player (say player 1, who is X)
# wants to place an X on the screen, they can’t just click on a terminal. So we are going to 
# approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board. 

# In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

# - Draw the Tic Tac Toe game board
# - Checking whether a game board has a winner
# - Handle a player move from user input
# The next step is to put all these three components together to make a two-player Tic Tac Toe game! 
# Your challenge in this exercise is to use the functions from those previous exercises all together 
# in the same program to make a two-player game that you can play with a friend. There are a lot of choices 
# you will have to make when completing this exercise, so you can go as far or as little as you want with it.

def draw_line(width, edge, filling):
    	print(filling.join([edge] * (width + 1)))


def display_winner(player):
	if player == 0:
		print("Tie")
	else:
		print("Player " + str(player) + " wins!")

def check_row_winner(row):
	"""
	Return the player number that wins for that row.
	If there is no winner, return 0.
	"""
	if row[0] == row[1] and row[1] == row[2]:
		return row[0]
	return 0

def get_col(game, col_number):
	return [game[x][col_number] for x in range(3)]

def get_row(game, row_number):
	return game[row_number]

def check_winner(game):
	game_slices = []
	for index in range(3):
		game_slices.append(get_row(game, index))
		game_slices.append(get_col(game, index))

	# check diagonals
	down_diagonal = [game[x][x] for x in range(3)]
	up_diagonal = [game[0][2], game[1][1], game[2][0]]
	game_slices.append(down_diagonal)
	game_slices.append(up_diagonal)

	for game_slice in game_slices:
		winner = check_row_winner(game_slice)
		if winner != 0:
			return winner

	return winner

def start_game():
	return [[0, 0, 0] for x in range(3)]

def display_game(game):
	d = {2: "O", 1: "X", 0: "_"}
	draw_line(3, " ", "_")
	for row_num in range(3):
		new_row = []
		for col_num in range(3):
			new_row.append(d[game[row_num][col_num]])
		print("|" + "|".join(new_row) + "|")


def add_piece(game, player, row, column):
	"""
	game: game state
	player: player number
	row: 0-index row
	column: 0-index column
	"""
	game[row][column] = player
	return game

def check_space_empty(game, row, column):
	return game[row][column] == 0

def convert_input_to_coordinate(user_input):
	return user_input - 1

def switch_player(player):
	if player == 1:
		return 2
	else:
		return 1

def moves_exist(game):
	for row_num in range(3):
		for col_num in range(3):
			if game[row_num][col_num] == 0:
				return True
	return False

if __name__ == '__main__':
	game = start_game()
	display_game(game)
	player = 1
	winner = 0  # the winner is not yet defined


	while winner == 0 and moves_exist(game):
		print("Current player: " + str(player))
		available = False
		while not available:
			row = convert_input_to_coordinate(int(input("Choose row (1, 2, 3): ")))
			column = convert_input_to_coordinate(int(input("Choose column (1, 2, 3): ")))
			available = check_space_empty(game, row, column)
		game = add_piece(game, player, row, column)
		display_game(game)
		player = switch_player(player)
		winner = check_winner(game)
	display_winner(winner)