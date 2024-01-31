#A
#  At the top of your file write
# import time
# and use “time.sleep(1)” between each print line (it makes python
# pause for 1 second before progressing through the code).
# Make a load bar that start with the empty line
# | |
# for each second prints and extra load bar “=”, hence after 3second
# should look like this
# |===> |
# and ends with a full bar
# |==========|
# Each line should be a new print of a raw string, so no use of for-loops
# or fancy string operation! e.g. the 5
# th print will simply be
# print(“|===> |”)

import time

print(r"| |")
time.sleep(1)
print(r"|=> |")
time.sleep(1)
print(r"|==> |")
time.sleep(1)
print(r"|===> |")
time.sleep(1)
print(r"|====> |")
time.sleep(1)
print(r"|=====|")
time.sleep(1)

#B
# For all lines, use the print-function end-parameter
# end = ”” (no new line)
# and
# add “\r” in the beginning of each string for a new print (revert the
# marker back to the beginning of the line). E.g. for the 5th print
# print(“\r|===> |”, end=””)
# This overwrite the text from the previous line (except the final line
# where you can use default end).
# Finish by printing “Done!”