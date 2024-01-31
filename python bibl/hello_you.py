# Ask user for name
name = input("What is your name?: ")

# Ask for age
age = input("What is your age?: ")

# Ask user for city

city = input("What city?: ")

# Ask user what they enjoy

love = input("What do you love?: ")

# Create output text

string = "Your name {}, and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,love)

# Print output to screen
print(output)
