def main():
    # Create an empty dictionary
    name_age_dict = {}

    # Instructions to user
    print("Enter a name followed by an age. (e.g., 'Kristoffer 33')")
    print("Enter a name to get the age of the person.")
    print("Type 'PRINT' to display the contents of the dictionary.")
    print("Press Ctrl+C to stop the program.")

    while True:
        try:
            # Read input from the user
            user_input = input("INPUT: ")

            # Split input into parts
            parts = user_input.split()

            # If the user types PRINT
            if user_input == "PRINT":
                for name, age in name_age_dict.items():
                    print(f"Our candidate {name} is {age} years old")
                continue

            # Check if there are more than 2 elements separated by SPACES
            if len(parts) > 2:
                print("OUTPUT: {}")  # Print empty dictionary
                continue

            # If user_input contains both name and age
            if len(parts) == 2:
                name, age = parts
                # Add to dictionary
                name_age_dict[name] = age
                print(f"OUTPUT: {name_age_dict}")

            # If user_input contains only name
            elif len(parts) == 1:
                name = parts[0]
                # Fetch age from dictionary
                if name in name_age_dict:
                    print(f"OUTPUT: {name_age_dict[name]}")
                else:
                    print(f"The age of {name} is unknown")

        except KeyboardInterrupt:
            # Handle Ctrl+C to stop the loop and exit
            print("\nExiting program.")
            break

if __name__ == '__main__':
    main()
