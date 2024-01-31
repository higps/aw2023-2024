while True:
    choice = input("Write your own string? y/n: ").strip().lower()
    if choice == 'y':
        string = input("Enter your string with words encapsulated with # or _ for changes to happen: ")
        break
    elif choice == 'n':
        string = "Everyone _said_ that it would not work. Then someone came, #UNAWARE# of what everyone said, and just did it."
        break

# split input string
parts = string.split()

# Initialize an empty list to store the string that gets changed by the code

modified_parts = []

# Variable in case we need to change the symbols later
underscore = "_"
hashtag = "#"

for word in parts:
    # Using the method from the hint
    if word.startswith(underscore) and word.endswith(underscore):
        
        modified_word = word[1:-1].upper()
        modified_parts.append(modified_word)
    # Remove hash same as above but set to lower instead, but using slices instead
    elif word[0] == hashtag and word[-1] == hashtag:
        
        modified_word = word[1:-1].lower()
        modified_parts.append(modified_word)
    else:
        # All other words are just appended as is
        # Remove words with unencapsulated tags like #word and word_ but don't alter the captialization of the word
        modified_word = word.replace(underscore, '').replace(hashtag, '')
        #print(modified_word)
        modified_parts.append(modified_word)
        

modified_string = " ".join(modified_parts)

print(modified_string)


#if statements

#formatting

#output string
