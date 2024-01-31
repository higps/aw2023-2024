# Make a program called my_sum.py. Use the “input” operation in
# python, and let the user specify two inputs, sum them together, and
# print the result. Double check that the math is correct.
# hint: make sure that the type of the values is float (and not string)
# before adding them together
var1 = input("Enter Value1: ")
var2 = input("Enter Value2: ")

# print(int(var1).isdigit())
# print(float(var1).isdecimal())
# ready = False
# while ready == False:
#     if ((var1.isdigit or var1.isdecimal) and (var2.isdigit or var2.isdecimal)):
#         ready = True
    
#     if not (var1.isdigit or var1.isdecimal):
#         var1 = input("Invalid value, Enter Value1 again: ")
    
#     if not (var2.isdigit or var2.isdecimal):
#         var2 = input("Invalid value, Enter Value2 again: ")
    

print(f"Sum: {float(var1)+float(var2)}")