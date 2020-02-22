# Exercises 33, 34, 35 and 36

# For this exercise, we will keep track of when our friend’s birthdays are, and 
# be able to find that information based on their name. Create a dictionary (in your file) 
# of names and birthdays. When you run your program it should ask the user to enter a name, 
# and return the birthday of that person back to them.

# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
# In this exercise, load that JSON file from disk, extract the months of all the birthdays, 
# and count how many scientists have a birthday in each month.

#  Load the JSON file from disk, extract the months of all the birthdays, 
#  and count how many scientists have a birthday in each month.

# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists 
# have birthdays in! Because it would take a long time for you to input the months of various scientists, 
# you can use my scientist birthday JSON file. Just parse out the months 
# (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.

birthdays = {
    "Fede": "09/12/1990", 
    "Juli": "02/27/1993", 
    "Patri": "06/03/1962"
}
import bokeh.plotting
import json
from collections import Counter

num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)


print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print(name)

newName = input("New person's name: ")

if newName not in birthdays.keys():
    newBirthday = input("New person's birthday: ")
    birthdays[newName] = newBirthday
else:
    print("That person's birthday was already added.")

# print(birthdays)

months = []
for name, birthday_string in birthdays.items():
    month = int(birthday_string.split("/")[0])
    months.append(num_to_string[month])

months = Counter(months)
# print(months)

with open('birthdays.json', 'w') as f:
    json.dump(birthdays, f)
print('{} was added to the birthday list\n'.format(newName))

months_name = list(months.keys())
months_quantity = list(months.values())

bokeh.plotting.output_file('plot.html')
plot = bokeh.plotting.figure(x_range=list(num_to_string.values()))
plot.vbar(x=months_name, top=months_quantity, width=0.7)
bokeh.plotting.show(plot)

name = input("Who's birthday do you want to look up?: ")
if name in birthdays:
    print('{}\'s birthday is {}.'.format(name, birthdays[name]))
else:
    print('Sadly, we don\'t have {}\'s birthday.'.format(name))

