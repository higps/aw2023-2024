import datetime

#Get the current year
current_date = datetime.datetime.now()
current_year = int(current_date.strftime("%Y"))


#Set age variables
drinking_age_norway = 18
drinking_age_usa = 21

drinking_year_norway = current_year - drinking_age_norway
drinking_year_usa = current_year - drinking_age_usa

name = input("What is your name?: ").title()
# Split the input into a list of names
names_list = name.split()

# Check if there are at least two names
while not len(names_list) >= 2:    
    name = input("Please enter first and last name: ").title()
    names_list = name.split()
    


born_year = input("What year were you born?: ")

# Ensure that the user enters a valid value as year
while not born_year.isdigit():
    born_year = input("Please enter the year you were born with numbers: ")
    
born_year = int(born_year)
location = input("Where do you live? :")

current_age = current_year - born_year

# Modify the strings here as we say the same strings multiple times in the later if statements
age_string = f", because you are {current_age} years old"
you_can = "you are allowed to drink in"
you_can_not = you_can.replace("are", "aren't")


if location.upper() == 'USA':
    location = location.upper()
    if born_year <= drinking_year_usa:
        
        print(f"{name}, {you_can} the {location}{age_string}")
    else:
        print(f"{name}, {you_can_not} the {location}{age_string}")
elif location.upper() == 'NORWAY':
    location = location.capitalize()
    if born_year <= drinking_year_usa:
        
        print(f"{name}, {you_can} {location}{age_string}")
    else:
        print(f"{name}, {you_can_not} {location}{age_string}")
else:
    print("No known location was given, unable to determine drinking age legality")
    
