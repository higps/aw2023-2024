
dictionary = {}


while True:
    user_input = input("Enter your data: ").strip()
    printed = False
    if user_input == "PRINT":
        print(dictionary)
        printed = True

    if user_input == "END":
        print("Ending program")
        break

    # Parts becomes a list here
    parts = user_input.split()

    
    if len(parts) != 2 and not printed:
        print(f"ERROR, incorrect amount of arguments. Expected 2, got {len(parts)}")
    elif len(parts) == 2:

        key, value = parts[0], parts[1]
        #if there is no key in dictoary
        if key not in dictionary:
            # make sure the value is always a list so we can append later
            dictionary[key] = [value]
        else:
        # key exists, append list elements
            dictionary[key].append(value)
        


