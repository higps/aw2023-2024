people = {}

while True:
        # Could not find a good method to use name, age = input() initalization without using a ton of stuff we haven't looked at yet when handling errors.
        # I gather it all in one string and split accordingly instead to get the desired result
        user_input = input("Enter name and age or just name to get age: ").capitalize()

        # With this setup it's possible to name a person PRINT as long as there something more to PRINT, like Printy
        if user_input.upper() == "PRINT":
            # Loop through name and age in dictionary
                for name, age in people.items():
                    print(f"{name} is {age} years old")
                continue
        
        # Split the input in to parts to work with
        parts = user_input.split()

        # If only 1 parameter was entered
        if len(parts) == 1:
            name = parts[0]

            if name in people:
                print(people[name])
            else:
                print(f"Age is unknown for {name}")

        elif len (parts) == 2:
            name, age = parts
            if age.isdigit():
                people[name] = age
                print(people)
            else:
                print(f"Invalid input. Age must be a number. Age was {age}")
        #if there's more than 2 parts, it's an invalid format
        else:
            print("Invalid input. We only accept one name and one age")


            
