# Create a new python program where given two strings the first 2 letters of
# each strings a swapped, e.g:
# string_1 = “abcde”
# string_2 = “Kristoffer”
# should now become “Krcde” and “abistoffer”

string_1 = "abde"
string_2 = "Kristoffer"

#Only sets the new strings to one letter
# new_string_1 = string_2[0]
# new_string_2 = string_1[0]

#Does not work since you can't modify strings, only fully overwrite
# string_1[0] = new_string_2
# string_2[0] = new_string_1[0]

# Change the first two letters and add the rest of the string with 1: slice
new_string_1 = string_2[0] + string_1[1:]
new_string_2 = string_1[0] + string_2[1:]

print(new_string_1, new_string_2)