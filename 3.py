# Exercise 3
# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this 
# list in it and print out this new list.
# Ask the user for a number and return a list that contains only elements from the original list a that are
# smaller than that number given by the user.

import myFunctions
import random

numberList = myFunctions.random_number_list()
print(numberList)
lowerThan5List = []
lowerThanInputList = []

inputNumber = myFunctions.get_int("Enter a number: ")

def printLowerThan5(nList: list):
    print("Numbers lower than 5: ")
    for number in nList:
        if number < 5:
            print(number)
            lowerThan5List.append(number)
        if number < inputNumber:
            lowerThanInputList.append(number)

printLowerThan5(numberList)   
print("List of numbers lower than 5: " + str(lowerThan5List))
print("List of numbers lower than input: " + str(lowerThanInputList))