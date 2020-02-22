# Exercises 30, 31 and 32

# You can start your Python journey anywhere, but to finish this exercise you will have to have 
# finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).

# In this exercise, we will finish building Hangman. In the game of Hangman, 
# the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic 
# for guessing the letter and displaying that information to the user. In this exercise, we have 
# to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, 
# don’t penalize them - let them guess again.
# Optional additions:

# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art 
# for the Hangman. This is challenging - do the other parts of the exercise first!

from random import choice

def get_word():
    """
        Retrieve a word from sowpods.txt file
            - sowpods.txt file is a SOWPODS dictionary
        
        returns tuple
    """
    visible = ""
    
    # load 
    with open("sowpods.txt", 'r') as sowpods_file:
        words = sowpods_file.readlines()
        hidden = choice(words).strip()
    
    for elem in hidden:
        visible += "_"
        
    return hidden, visible


def draw_board(inc_guesses, vis_word):
    """
        Displays the hangman, a list of previous incorrect guesses, and 
            a dashed out word w/ letters in places where correctly guessed
            
        returns string
    """
    vis_word = ' '.join(vis_word)
    num_wrong_guesses = len(inc_guesses)
    incorrect_letters = ', '.join(inc_guesses)
    
    for i in range(20):
        print("\n")
    
    print("  +=====+          " + vis_word)
    print("  |     '")
    if num_wrong_guesses >= 1:
        print("  |     O           Incorrect Guesses:")
    else:
        print("  |                 Incorrect Guesses:")
    if num_wrong_guesses == 6:
        print("  |    /|\               " + incorrect_letters)
    elif num_wrong_guesses == 5:
        print("  |    /|                " + incorrect_letters)
    elif num_wrong_guesses >= 2:
        print("  |     |                " + incorrect_letters)
    else:
        print("  |                      " + incorrect_letters)
    if num_wrong_guesses >= 4:
        print("  |    / \\")
    elif num_wrong_guesses == 3:
        print("  |    /")
    else:
        print("  |")
    print("  |")
    print("==========")
    
    
def get_guess():
    """
        Prompt user for a guess. User can also start a new game or exit out of program.
        
        returns string
    """
    letter = input("What letter would you like to guess? (Quit) | (Reset)  ")
    while ((not letter.isalpha())
           or (letter.lower() not in ('quit', 'reset') and len(letter) != 1)):
        # invalid input detected
        letter = input("You may type quit to end game, reset to start a new game (get new"
                       + " word), or a letter if you would like to continue playing/guessing.  ")
        
    return letter.upper()


def check_guess(guess, hidden_word, vis_word, inc_guesses):
    """
        Check whether guess is in hidden_word or not
        
        If in hidden_word, add to vis_word
        If not in hidden_word, add to inc_guesses
        
        returns tuple
    """
    vis_word = list(vis_word)
    hid_word = list(hidden_word)
    
    if guess not in inc_guesses and guess not in vis_word:
        # has not been attempted/guessed before
        if guess in set(hid_word):
            for i, elem in enumerate(hid_word):
                if guess == elem:
                    vis_word[i] = guess
        else:
            inc_guesses.append(guess)
    
    return ''.join(vis_word), inc_guesses


def play_again():
    """
        Prompt user if he/she would like to play another game.
        
        returns bool
    """
    another_game = input("Would you like to play again? (y)es | (n)o ")    
    while another_game.lower() not in ('y', 'n'):
        # invalid input detected
        another_game = input("Press y to play again, n to quit.")
        
    if another_game.lower() == 'y':
        return True
    else:
        return False


def main():
    quit_game = False
    new_game = True
    
    while not quit_game:
        if new_game:
            # reset game variables
            incorrect_guesses = []
            hidden_word, visible_word = get_word()
            new_game = False
        else:
            # continuation of game
            draw_board(incorrect_guesses, visible_word)
            guess = get_guess()
            
            if guess == 'QUIT':
                print("Thank you for playing! Good bye!")
                quit_game = True
                continue
            elif guess == 'RESET':
                new_game = True
                continue
            else:                
                # check if correct guess
                visible_word, incorrect_guesses = check_guess(guess, hidden_word, visible_word, incorrect_guesses)
                
                # check if win
                if visible_word == hidden_word:
                    draw_board(incorrect_guesses, visible_word)
                    print("Congratulations!")
                    
                    if play_again():
                        new_game = True
                    else:
                        print("Thank you for playing! Good bye!")
                        quit_game = True

                # check hangman
                if len(incorrect_guesses) == 6:
                    draw_board(incorrect_guesses, hidden_word)
                    print("Hangman!")
                    
                    if play_again():
                        new_game = True
                    else:
                        print("Thank you for playing! Good bye!")
                        quit_game = True
            

if __name__ == "__main__":
    main()