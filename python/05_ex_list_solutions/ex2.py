import random

dice = [1,2,3,4,5,6]
n_dices = 5

rand_dices = random.choices(dice, k=n_dices)

if min(rand_dices)==max(rand_dices):
    print('Yeah you got Yahtzee!')
else:
    print('No Yahtzee, try again')

print(f'Min dice value: {min(rand_dices)}')
print(f'Max dice value: {max(rand_dices)}')
print(f'Here are the dices: {sorted(rand_dices)}')

