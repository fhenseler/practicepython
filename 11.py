# Exercise 11
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity 
# to practice using functions, described below.

import myFunctions

num = myFunctions.get_int('Insert a number: ')
if myFunctions.is_prime(num):
    print("The number", num, "is prime")
else:
    print("The number", num, "is NOT prime")