# Exercise 14
# Write a program (function!) that takes a list and returns a new list that contains 
# all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

numberList = [1, 2, 3, 3, 4, 4, 5, 6]

def removeDuplicates(list) -> list:
    noDuplicatesList = []
    for number in list:
        if number not in noDuplicatesList:
            noDuplicatesList.append(number)
    return noDuplicatesList

print("Original List: " + str(numberList))
print("List without Duplicates: " + str(removeDuplicates(numberList)))
print("No duplicates using sets: " + str(list(set(numberList))))

# Exercise 5 part
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new = a + b
print ("Exercise 5 set: " + str(list(set(new))))

