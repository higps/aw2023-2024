# a)
# Go back to ex2_str.docx exercise 3. And again,
# encapsulate the code for exercise a), in function
# called “bart_cheat_code” which should takes two
# inputs, “numb_of_repetition” and “punishment_text”
# and return the string.
# Call the function with a variety of inputs and verify
# that it works.

def bart_cheat_code(numb_of_repetition, punishment_text):
    return ((punishment_text+'\n')*numb_of_repetition)    


punishment_text = "I will not teach others to fly"
numb_of_repetition = 25
# b)
# Set a default for “numb_of_repetition” to 10.
# test that it works.
numb_of_repetition = 10

print(bart_cheat_code(numb_of_repetition, punishment_text))