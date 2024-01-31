a = [1,2,3]

def f1():
    a[0] = 5 # can override global variables
    print(a)
    
def f2():
    a = 50 #local
    print(a)

def f3():
    global a
    a = 20
    print(a)

f1()
f2()
print(a)
