# Write a code for the game of guessing the number
# someone is thinking of. The task is completed when:
# a. Takes a target number as input by a user and save it
# in a variable.

target_num = int(input("Enter target num: "))

# b. Take another input, number of allowed wrong
# guesses.

wrong_numb_guess = int(input("Enter number of wrong inputs: "))

# c. Clear the terminal such that the person guessing
# cannot see the target number.

print(chr(27) + "[2J")

# d. The user should try to guess the number, and after
# each guess the algorithm should print the number of
# tries left, as well as the information if the guess is too
# large or small.
guess_count = 0

def attempts_left(guess_count):
    return wrong_numb_guess-guess_count


# e. The code should stop when the person guesses the
# number, or the total number of tries reaches the
# limit.
# Print a suitable message for each of the two cases

not_guessed = True
not_out_of_attempts = True
while not_guessed or not_out_of_attempts:
    guessed_num = int(input("Guess number: "))
    guess_count += 1
    if(guessed_num == target_num):
        print(f"Congratulations you guessed the number was {target_num}")
        not_guessed = False

    if(guess_count >= wrong_numb_guess and not_guessed == True):
        not_out_of_attempts = False
        print("You lose, Out of attempts")

    if (guessed_num > target_num):
        print(f"{guessed_num} is bigger than the target number")
    elif(guessed_num < target_num):
        print(f"{guessed_num}, is smaller than the target number")
    
    print("Attempts left: ",attempts_left(guess_count))


