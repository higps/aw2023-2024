# Go back to “ex01_print_and_var.docx” question 4.
# Define 3 variables:
# current_number, total_numb, bar_length.
# These variables should define the bar print.
# Change the code such that only one line is printed.
# Example:
# say bar_length is set to 10, current_number is 50 and total_numb is 100
# then the code should print
# |=====> |
# |======>   |
# |          |
# where the bar is half way, and the total length of the bar is 10 characters.
import time
current_number = 100
total_number = 100
bar_lenght = 10

progress =  int(current_number/total_number*bar_lenght)
equalsigns = progress -1
bar = bar_lenght-progress
crock = '>'

if(current_number==total_number):
        crock=''
        equalsigns = progress
#calculate how many =, subtract from spaces
#make the last = a > and fill the rest with spaces
#gives the correct empty space
my_string = '|'+ ('=' * equalsigns) + crock + " " * bar + "|"
print(len(my_string))
print(my_string)

