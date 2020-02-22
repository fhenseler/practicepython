# Exercise 1
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies 
# of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. 

import datetime
import myFunctions

def hundred_years_calculator(age) -> int:
    now = datetime.datetime.now()
    currentYear = now.year
    finalDate = currentYear + 100 - age
    return finalDate

def multiple_print(times, date, name):
    while times > 0:
        print("Dear " + name + ", you will turn 100 years old on " + str(date))
        times -= 1

if __name__=="__main__":

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    date = hundred_years_calculator(age)
    copy_message = myFunctions.get_int("How many times you want to print the message: ")
    multiple_print(copy_message, date, name)