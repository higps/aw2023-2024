known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]

#print(len(known_users))

print("Bob2" in known_users)

#Only removes first instance
#Can use del list[x] directly
#del example[0:2] slice

while False:
    print("Hi My name is Travies")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print(f"Hello {name}")
        remove = input("Would you like to be removed from the system (y/n): ").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == 'n':
            print("No problem")
    else:
        print(f"hmm I don't I have you yet{name}")
        add = input("Would you like to be added to the system (y/n/)").strip().lower()
        if add == 'y':
            known_users.append(name)
        elif remove == 'n':
            print("No worries, see you around")
            

#Only lists can be added to lists

A =[5,12,72,55,89]
#A = A + 1 #doesnt work
A = A + [1] #works
A = A + ["STRING"]#works
A = A + list("BCD")


A = A + list(str(123))

print(A)


A = A + [[5,6,7,9]]

print (A[-1])



A.append([10,11,12,13])

print (A)
A = [5,12,72,55, 89, 1]
#do not do: A = A.append(10)

print("A: ", A)


A.insert(2,100)

A.insert(2,[10,30,20])
