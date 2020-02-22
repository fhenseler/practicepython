# Exercise 28

# Implement a function that takes as input three variables, 
# and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally 
# takes care of for us. All you need is some variables and if statements!

def maxNumber(num1, num2, num3) -> int:
    max = 0
    if num1 > num2:
        max = num1
    elif num1 < num2:
        max = num2
    else:
        max = num1

    if max < num3:
        max = num3

    return max

print("Max number is:", maxNumber(2, 7, 8))

# Another solution is making a list then sorting it