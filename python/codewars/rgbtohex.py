def rgb(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(max(0, min(255, round(r))),max(0, min(255, round(g))), max(0, min(255, round(b)))).upper()
    # your code here :)


# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
#  Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
# R/16 = x + y/16
# G/16 = x' + y'/16
# B/16 = x" + y"/16
print(rgb(1, 2, 3))
print(rgb(-20, 275, 125))