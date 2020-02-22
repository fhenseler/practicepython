# Exercise 6
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

import myFunctions

word = myFunctions.get_str("Insert a word: ")
wordLower = word.lower()
wordLength = len(word)
reverse = ""

for index in range(wordLength):
    reverse += wordLower[wordLength-1-index]

if myFunctions.check_palindrome(wordLower, reverse):
    print("The word " + word + " is a palindrome")
else:
    print("The word " + word + " is NOT a palindrome")