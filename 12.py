# Exercise 12
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new
# list of only the first and last elements of the given list. For practice, write this code inside a function.

import myFunctions

numberList = myFunctions.random_number_list(5)

def firstLast(numList: list) -> list:
    first = numList[0]
    last = numList[len(numList) - 1]
    numList.clear()
    numList.extend([first, last])
    return numList

# Using List Comprehensions
def firstLast2(numList: list) -> list:
    return [numList[0], numList[-1]]

print(numberList)
print(firstLast(numberList))
print(firstLast2(numberList))
print(myFunctions.first_and_last(numberList))
