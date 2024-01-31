# Create a variable with a string assigned e.g. my_string = “hello world”.
# Removes the first and last characters of the string, and then print the
# output. For example:
# Output: “ello worl”

my_string = "Hello World"

#Just slicing
new_string = my_string[1:-1]
print(new_string)

#replacing
my_string = my_string.replace(my_string[0], "")
my_string = my_string.replace(my_string[-1], "")
print(my_string)
