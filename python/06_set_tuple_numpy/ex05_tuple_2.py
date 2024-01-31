# 2. Ash Ketchum have been out capturing Pokémon’s again.
# He first got a Pikachu, then Pidgey, then Abra, then Pidgey,
# then Eevee then Pidgey
# a. Make a tuple called “captured”, with the captured
# Pokémon’s (make sure to keep the orders they was
# captured)

captured = 'Pikachu', 'Pidgey', 'Abra', 'Pidgey', 'Eevee', 'Pidgey'

print(captured)
# b. Would it have been favorable to use a list instead of
# tuple in this case? What is the pros and cons?

#If it is a tuple we can't alter the values, but if it's a list then we could alter the order

# c. Ash memory is not as it used to be, He is wondering if
# there might be multiple pidgeys from the captured
# tuple. Use the count method and print the number of
# pidgeys in the list.
# Set:

print(captured.count('Pidgey'))

# d. Since Ash memory is going bad, Help him and create a
# program that takes a user input (using the python
# input operator), where the user can type a Pokémon
# name and then the program should print out if the
# Pokémon is already in the captured tuple or not.
# also print the total number of Pokémon’s in the
# captured tuple, as well as the number of unique.

input = input("Type Pokemon name?: ").title()

if input in captured:
    print(f"There was {captured.count(input)} Pokemon of that type captured")

print(f"Total number of pokemon was {len(captured)}")