# Exercise 4
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides 
# evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

import myFunctions

def generateDivisorList(number: int):
    divisorList = []
    for i in range(number, 0, -1):
        if number % i == 0:
            divisorList.append(int(number / i))
    print("List of divisors for number " + str(number) + " : " + str(divisorList))

generateDivisorList(myFunctions.get_int("Insert number: "))