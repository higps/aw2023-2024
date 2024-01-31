students = {
    "Alice":{"id":"ID001", "age":26, "grade":"A"},
    "Bob":{"id":"ID002", "age":27, "grade":"B"},
    "Claire":{"id":"ID003", "age":17, "grade":"C"},
    "Dan":{"id":"ID004", "age":21, "grade":"D"},
    "Emma":{"id":"ID005", "age":22, "grade":"E"}
    }

#all data
#print(students["Claire"])

#just id
#print(students["Claire"][0])


#getting age and grade starting at index 1 and going to the end with slices
print(students["Dan"]["age"])
print(students["Emma"]["id"], students["Emma"]["grade"])
