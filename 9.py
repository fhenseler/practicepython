# Exercise 9 
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
import myFunctions

number = random.randint(1, 9)
userResponse = ''
userNumber = 0
keepPlaying = True
guessCounter = 0

while keepPlaying == True:
    userNumber = myFunctions.get_int("Guess the secret number from 1 to 9: ")
    if userNumber == number:
        print("You Win!")
        guessCounter += 1
        break
    elif userNumber < number:
        print("Your guess was too low. Keep trying!")
        guessCounter += 1
    elif userNumber > number:
        print("Your guess was too high. Keep trying!")
        guessCounter += 1
    
print("Secret number: " + str(number))
print("Number of guesses: " + str(guessCounter))