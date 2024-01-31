# a. Create 3 variables var_1, var_2 and var_3 giving them
# the values 1, 2 and 3 respectively using only a single
# line of code in python.

var_1, var_2, var_3 = 1,2,3


# b. Change the value of var_1 and var_2 such that
# var_1= var_2 and var_2= var_1. print the values to
# verify that now var_1=2 and var_2=1.
# (hint: you might need temporary variables)

var_1, var_2, var_3 = 1,2,3

var_1, var_2 = var_2, var_1

# c. In most programming languages you need temporary
# variables for handling variables “switches” such as in
# b, but python offers a way to do this without!
# try changing the code in b to
# var_1, var_2 = var_2, var_1
# and verify that this method also work. 

