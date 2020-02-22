# Exercise 20
# Write a function that takes an ordered list of numbers (a list where the elements are in order 
# from smallest to largest) and another number. The function decides whether or not the given number 
# is inside the list and returns (then prints) an appropriate boolean.

# Extras:
# Use binary search.

import myFunctions

def regularSearch(number, list) -> bool:
    numberExists = False
    if number in list:
        numberExists = True
    return numberExists

# Binary Search
def find(alist,number):
    start_index = 0
    end_index = len(alist)
    while True:
        middle_index = (end_index + start_index) // 2
        if number == alist[middle_index]:
            return True
        elif middle_index == start_index:
            return False 
        elif number < alist[middle_index]:
            end_index = middle_index
        else:
            start_index = middle_index

if __name__=="__main__":
    orderedList = [1, 2, 5, 9, 16, 22, 24]
    number = myFunctions.get_int("Enter number: ")

    if regularSearch(number, orderedList):
        print("Regular Search: The number " + str(number) + " is in the list " + str(orderedList))
    else:
        print("Regular Search: The number " + str(number) + " is NOT in the list " + str(orderedList))
    
# Binary   
a = [0, 1, 3, 4, 5, 6, 7, 8, 9]
print(find(a, 0))  # returns True
print(find(a, -1)) # returns False
print(find(a, 12)) # returns False
print(find(a, 2))  # returns False
print(find(a, 1))  # returns True


######################################################################################################