# Exercise 5
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are 
# common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random
import myFunctions

randomlist1 = myFunctions.random_number_list()
randomlist2 = myFunctions.random_number_list()

commonList = []

for num in randomlist1:
    if num in randomlist2 and num not in commonList:
        commonList.append(num)

print("randomlist1: " + str(randomlist1))
print("randomlist2: " + str(randomlist2))
print("List of common elements between both lists - no duplicates: " + str(commonList))