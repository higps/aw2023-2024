# Make a upper and lower quantile calculator.
# The goal is to create a program that can find the upper and
# lower interval of a list of number (like a numerical
# confidence interval), based on some confidence level.

# a)
# Start by defining the variables
# i. values (which is a list of random number, you
# can type in yourself)
# ii. alpha (a number between 0 and 1)
import random
list_len = random.randrange(5, 500)
random_list = random.sample(range(100), list_len)
#values = [1,5,4,1,2,3,5,7,8,91,102,5,23,56,45,62,3,15]
alpha = 0.5

print(random_list)

#b)
# Sort the list of values.
random_list.sort()
# c)
# The next step is to extract the two indexes that
# defines the lower and upper interval given some
# alpha, such that the middle 1-alpha amount of the
# values lands within the middle.
# calculate the lower and upper index by:
# lower_idx = round(n*alpha/2)
# upper_idx = round(n*(1-alpha/2))-1
# where n is the length of the value list. Remember the
# “round” as indexes require integers to work with list.

n = list_len
lower_idx = round(n*alpha/2)
upper_idx = round(n*(1-alpha/2))-1


# d)
# Use the sorted list to extract the lower and upper
# values, and print them.

print("Lower:", random_list[:lower_idx])
print("Upper:", random_list[upper_idx:])