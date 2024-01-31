films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What film do you want to see?: ").strip().title()

    if choice in films:

        print("Available seats: ",films[choice][1])
        age = int(input("How old are you?").strip())
            
        #check user age
        if age >= films[choice][0]:

            #check seat numbers

            if films[choice][1] > 0:
                print("Enjoy the film")
                films[choice][1] -= 1
            else:
                print("No seats available")
        else:
            print("You are too young to see that film")
    else:
        print("We don't have that film...")
