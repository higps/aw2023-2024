# Create funciton called my_counter that takes a single parameter

def my_counter(param):
    #make sure parameter is list or string
    if not isinstance(param, (list,str)):
        raise ValueError(f"Parameter must be a list or a string. Parameter was {param}")
    
    dict = {}
    #this is a string

    for key in param:
        if key not in dict:
            dict[key] = 1
        else:
            #get the value of key and set it to +1
            dict[key] += 1
    return print(dict)


my_counter("hello") #returns a dict: {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}
my_counter("lallala")# returns a dict: {‘l’: 4, ‘a’: 3}
my_counter([1, 2, 1, 3]) #returns a dict: {1: 2, 2: 1, 3: 1}

