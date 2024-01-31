# Guessing game
import os
def guessing_game():
    fasit = int(input("Type the number to guess: "))

    allowed_attempts = int(input("Allowed attempts: "))

    os.system('cls')

    guess_count = 0
    is_complete = False
    while allowed_attempts>guess_count and not is_complete:
        user_guess = int(input("Guess a number: "))
        guess_count += 1
        remaining_attempts = allowed_attempts - guess_count
        if user_guess == fasit:
            print("Congratulations, you guessed the correct number")
            is_complete = True
        elif user_guess > fasit:
            print(f"Feil, for stor! Du har {remaining_attempts} forsøk igjen")
        elif user_guess < fasit:
            print(f"Feil, for liten! Du har {remaining_attempts} forsøk igjen")

    if not is_complete:
        print("Du failet, bad, LOSER!")


guessing_game()
    