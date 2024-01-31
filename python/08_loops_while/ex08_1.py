# a. Change the logic such that the code still creates a
# repeating string, but do it using a while loop.
# Call the function “bart_cheat_code_while”.
# hint: create the code first, than encapsulate it in a
# function.


punishment_text = "I will not teach others to fly"
numb_of_repetition = 25

def bart_cheat_code_while(punishment_text):
    return (punishment_text)

count = 1
while count <= numb_of_repetition:
    print(bart_cheat_code_while(punishment_text))
    count += 1

# b. Do the same as above, but use a for-loop and call the
# function “bart_cheat_code_for”

def bart_cheat_code_for(punishment_text):
    return (punishment_text)


for i in range(numb_of_repetition):
    print(bart_cheat_code_for(punishment_text))