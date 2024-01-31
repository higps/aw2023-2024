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
x = input("Enter Value1: ")
op = input("Enter math operator: ")
y = input("Enter Value2: ")



print(calculator(x,y,op))

