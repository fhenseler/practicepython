# Exercise 22
# Given a .txt file that has a list of a bunch of names, count how many of each name there are 
# in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

# Extra:

# Instead of using the .txt file from above (or instead of, if you want the challenge), 
# take this .txt file, and count how many of each “category” of each image there are. 
# This text file is actually a list of files corresponding to the SUN database scene recognition 
# database, and lists the file directory hierarchy for the images. Once you take a look at the 
# first line or two of the file, it will be clear which part represents the scene category.

def count_cat(filename):
	categories = {}
	with open(filename, "r") as file:
		line = file.readline()[3:-26]
		while line:
				if line in categories.keys():
						categories[line] += 1
				else:
						categories[line] = 1
				line = file.readline()[3:-26]
	return categories

print(count_cat("22.txt"))

