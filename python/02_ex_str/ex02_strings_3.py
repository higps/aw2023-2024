# By specifying the variables
# punishment_text = “I will not teach others to fly”
# and
# numb_of_repetition = 25
# the program should print the same “punishment_text” the
# “numb_of_repetition” just like you see in the picture.
# Use anything learned until now (while/for loops and lists are not
# allowed in this exercise). Remember to add a line shift (“/n”) for each
# time punishment line is written.
# Hint: how can you make the string repeat itself without a loop (see
# slide if you can’t recall)

## A)

punishment_text = "I will not teach others to fly, that I will be good"
numb_of_repetition = 25



print((punishment_text+'\n')*numb_of_repetition)

#for times in range(numb_of_repetition):
#    print(punishment_text+'\n')

# b. Mess with Bart, by writing code that removing the word “not” in
# “punishment_text”, and changing the word “good” with “bad”
# before its printed out.


print(punishment_text.replace('not ', ''))
print(punishment_text.replace('good', 'bad'))# good doesnt exist in the text


original_string = "Hello, world! This is a test."
substring_to_remove = "world"

# Using Slices to remove text
substring_to_remove = 'not'
original_string = "I will not teach others to fly"
start_index = original_string.find(substring_to_remove) #this finds the index of where the word starts
end_index = start_index + len(substring_to_remove) #this uses the start inex to find where the end index is

new_string = original_string[:start_index] + original_string[end_index+1:] #+1 needed since space between the words
print(new_string)

#Bart has a bad habit of using the word “that” to often. Add logic to
# the code such that the number of the word “that” is counted in
# “punishment_text”. Then after the multiple lines of
# “punishment_text” is printed, a single line with the information is
# printed with the following format
# “The number of the word THAT in the original sentence is: X”,
# with X replaced by the number.
substring = "that"
count = punishment_text.count(substring)
print(f"The number of the word {substring.upper()} in the original sentence is: {count}")