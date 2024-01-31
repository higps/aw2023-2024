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

import time
load = 5
start = '|'
end = '|'
loadbar = '='

print("| |", end="")
time.sleep(1)
print("|=> |")
time.sleep(1)
print("|==> |")
time.sleep(1)
print("|===> |")
time.sleep(1)
print("|====> |")
time.sleep(1)
print("|=====|")
time.sleep(1)

