students = {
    "male": ["Tom", "Charlie", "hHrry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }


#for key in students.keys():
    #print(key)
    #print(students[key])

for key in students.keys():
    for name in students[key]:
        if "a" in name.lower():
            print(name)
