# a. Create a list called students with at least 5 candidates
# from the class (with first name and last name,
# separated by space).

students = ['Marius Dyrseth', 'Bjarne Farne', 'Arne Bjarne', 'Fritjof Nilsen', 'Ole Jonny Ronny Reidar Roger','Tom Glover']

#b. Print the 3rd person. 
print(students[2])

#c. Print the first letter of the 3rd person.
print(students[2][0])

#d Change the name of the 3rd student to “Ole”
students[2] = 'Ole'

#e Add the last name “Nordmann” to Ole (from d).
students.insert(2,students[2]+" "+'Nordmann')

#f. Add the person you originally had in the 3rd position,
#but to the end of the students-variable.
students.append('Arne Bjarne')

# g Add a person called “Monty Python” at index 4, not
# just changing the name at position 4, but shifting the
# later students one index down.
students.insert(4, "Monty Python")

# h Print the length of the student list
# Remove “Ole Nordmann”
# and again print the length of the student list to verify
# that it’s one lower

print(len(students))
students.remove('Ole Nordmann')
print(len(students))

# i Get and print the index of the person called “Monty
# Python” now after the removal of “Ole Nordmann”.

print(students.index('Monty Python'))

# j Print the first 3 students
print(students[0:3])

# k Make a variable students_reverse where by using
# slicer, you reverse the students order
students_reverse = students[::-1]

# l Make a variable students_even where by using slicer,
# you only save the students at the even position (index
# 0, 2, 4) using slicer [start_idx : end_idx : step_size]
# m. Do the same as above, but odd indexes. 

students_even = students[0::2]
students_odd = students[1::2]


