# Make 5 variables, where each is a generated random
# integer between 1 and 6 (like dice).
# and print if the code generated a Yahtzee (check if all 5
# variables holds the same value)
import random
min = 1
max = 6


var1 = random.randint(min,max)
var2 = random.randint(min,max)
var3 = random.randint(min,max)
var4 = random.randint(min,max)
var5 = random.randint(min,max)

varlist = [var1,var2,var3,var4,var5]



yahtzee = False
dicerolls = 0
while not yahtzee:
    var1 = random.randint(min,max)
    var2 = random.randint(min,max)
    var3 = random.randint(min,max)
    var4 = random.randint(min,max)
    var5 = random.randint(min,max)
    #print(varlist)
    dicerolls += 1
    if var1 == var2 == var3 == var4 == var5:
        print(f"Yahtzee all numbers were {var1}, rolls {dicerolls}")
        yahtzee = True