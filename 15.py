# Exercise 15
# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

import myFunctions
inputString = myFunctions.get_str("Insert long text here: ")

def reverseString(string) -> str:
    splitString = string.split()
    reverse = []
    for word in splitString:
        reverse.insert(0, word)
    return " ".join(reverse)

print("Reverse: " + reverseString(inputString))

# One-line solution
def reverseWord(string):
  return ' '.join(string.split()[::-1])

print("One-liner:", reverseWord(inputString))