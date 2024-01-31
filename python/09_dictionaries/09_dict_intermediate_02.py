# Make a program that:
# a. Take an input by the user in console, using the format
# “key”;”value”. Hence an input with the two strings
# key and value split using “;”.

# b. Split the input on “;” and add the key value pair in a
# dictionary.

# c. Encapsulate the logic in a while loop, such that the
# program will ask for new inputs, until the input
# “revert” is given

# d. If a user write “revert” as input, first print the
# dictionary at hand, then add the revert key value pair
# in a new dictionary.

# eksample {‘hello’:’world’}, should be reverted to
# {‘world’: ‘hello’}.
# and print the new dictionary.

the_dict = {}
the_reverse_dict = {}
b_reverted = False

while not b_reverted:
    
    user_input = input("key; value").split(";")

    if "revert" in user_input:
        print(the_dict)
        b_reverted = True
        the_reverse_dict.update({value: key for key, value in the_dict.items()})
        print(the_reverse_dict)
    else:
        if (len(user_input) == 2): #Checks that the input length is more than one in case of invalid inputs
            the_dict.update({user_input[0]: user_input[1]})





