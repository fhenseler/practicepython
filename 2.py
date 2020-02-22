# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message 
# to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

import myFunctions

def even_check(number) -> str:
    if number % 4 == 0:
        result = "EVEN & MULTIPLE OF 4"
    elif number % 2 == 0:
        result = "EVEN"
    else:
        result = "ODD"
    return result

number = myFunctions.get_int("Enter a number: ")
result = even_check(number)
print("Dear user, number " + str(number) + " is " + result)

num = myFunctions.get_int("Enter another number: ")
check = myFunctions.get_int("Enter a number to divide the previous by: ")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)