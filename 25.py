# Exercise 25
# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 
# 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, 
# too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess. 
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) 
# until you hit the number. But that’s not an optimal guessing strategy. 
# An alternate strategy might be to guess 50 (right in the middle of the range), 
# and then increase / decrease by 1 as needed. After you’ve written the program, 
# try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

import myFunctions

def guess():
    i = 0
    # i is the lowest number in range of possible guess
    j = 100
    # j is the highest number in range of possible guesses
    m = 50
    # m is the middle number in range of possible guesses
    counter = 1
    # counter is the number of guesses take.
    print("Please guess a number")
    condition = myFunctions.get_int("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
    while condition != 1:
        counter += 1
        if condition == 0:
            i = m + 1
        elif condition == 2:
            j = m - 1
        m = (i + j) // 2
        condition = myFunctions.get_int("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
    print("It took" , counter , "time(s) to guess your number (", m ,")")
guess()
