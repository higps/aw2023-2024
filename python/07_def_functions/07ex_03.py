# Go back to ex4_if_else_bool.docx and encapsulate the
# calculator logic in a function called “my_calculator”. The
# function should take 3 inputs, “first_numb”, “operator”
# and “second_number”
# and return the calculated value.
# Make sure the code still takes inputs by the user and prints
# the result, but both the inputs and print should be outside
# the function.
# make sure the code still works as usual with the function.

def calculator(x,y,op):
    if not x.isnumeric():
        print(f"{x} is not numeric, use numbers")
        return False
    if not y.isnumeric():
        print(f"{y} is not numeric, use numbers")
        return False
    if op not in validops:
        print(f"{op} was not a valid operator")
        return False


    if (op == '+'):
        return float(x) + float(y)
    elif (op == "-"):
        return float(x) -float(y)
    elif (op == "*"):
        return float(x) * float(y)
    elif (op == "/"):
        if x or y == 0:
            print("Unable to devide by zero")
            return False
        return float(x) / float(y)

validops = "+-*/"
first_numb = input("Enter Value1: ")
operator = input("Enter math operator: ")
second_numb = input("Enter Value2: ")



print(calculator(first_numb ,second_numb, operator))

