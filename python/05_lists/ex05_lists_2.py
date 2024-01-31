# a)
#  Go back to ex4_if_else_bool.docx question 2, remove
# the 5 variables and make a new variable called dice
# which is a list of the values 1 to 6.
# Add a variable called n_dices which you can set to 5
# (as it is only 5 dices in Yahtzee).
# create a new variable called rand_dices using
# random.choices, dice and n_dice, which should holde
# n_dice random dice values. 
import random

dice = [1,2,3,4,5,6]
n_dices = 5

rand_dices = random.choices(dice, k = n_dices)

# c Also print the minimum dice value, max value and
# print the full list of dices, but after the list is sorted.

print(max(rand_dices),min(rand_dices),rand_dices)

#b) Fix the code such that the logic for checking if it is a
# Yahtzee using the rand_dices variable.


yahtzee = False
dicerolls = 0
while not yahtzee:
    rand_dices = random.choices(dice, k = n_dices)
    #print(varlist)
    dicerolls += 1
    if max(rand_dices) == min(rand_dices):
        print(f"Yahtzee all numbers were {rand_dices}, rolls {dicerolls}")
        yahtzee = True

