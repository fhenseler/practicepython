# Exercise 10
# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), 
# except require the solution in a different way.

# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common 
# between the lists (without duplicates). Make sure your program works on two lists of different sizes. 
# Write this in one line of Python using at least one list comprehension. 

# Extra:
# Randomly generate two lists to test this

import random
import myFunctions

listA = myFunctions.random_number_list()
listB = myFunctions.random_number_list(8) # Testing overloaded method
result_overlaps = [number for number in set(listA) if number in listB]
result = [number for number in result_overlaps if result_overlaps.count(number) == 1]

print("listA: " + str(listA))
print("listB: " + str(listB))
print("Overlaps: " + str(result))
    