name_list = []

while True:
    name = input("Enter a name: ")
    if name == 'PRINT':
        print(name_list)
    else:
        name_list.append(name)
        
    print("Use CTRL+C to exit program")
    
