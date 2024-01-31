# Go back to “ex3_numb_input.docx” question 4.
# and add logic, such that the code does not set “>” if the bar is completely empty or full. 
#
 

# The above logic is need such that we can call the bar multiple
# times in a row to generate an actual loading bar without
# printing each bar on a new line, and ensuring the length is correct

import time
current_number = 60
total_number = 100
bar_lenght = 10

progress =  int(current_number/total_number*bar_lenght)
equalsigns = progress-1
bar = bar_lenght-progress
crock = '>'

if(current_number==total_number)or(current_number==0):
        crock=''
        equalsigns = progress

my_string = '|'+ ('=' * equalsigns) + crock + " " * bar + "|"
#print(len(my_string))



# Add logic such that the print uses ‘end= “” ’ for all print except when the
# current_number equals total_numb then ‘end=”\n”’ (should print a new line).

# And also add logic such that the “home” parameter “\r” is used in the beginning of the
# string, except for the print when current_number=0. 

if (current_number==total_number):
      print(my_string, end="")
else:
       print(my_string, end="\n")