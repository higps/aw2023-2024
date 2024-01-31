# a 
students = ['Micheal Smith','Mary Johnson','James Williams','Jennifer Brown','Robert Garcia']

# b - 3rd person is in position 2 (first is a index 0)
print(students[2])

# c
# Solved in multiple steps:
person_numb3 = students[2]
person_numb3_first_letter = person_numb3[0]
print(person_numb3_first_letter)
# Equivalent solution, solved in a single step:
print(students[2][0])

# d
students[2] = 'Ole'

# e
students[2] = students[2]+' Nordmann'

# f 
students.append('James Williams')

# g
students.insert(4, 'Monty Python')
# Alternative way of doing it manually
students = students[0:4]+['Monty Python']+students[4:]

# h
print(len(students))
students.remove('Ole Nordmann')
print(len(students))

# i 
students.index('Monty Python')

# j 
print(students[0:3])

# k
print(students)
students_reverse = students[::-1]
print(students_reverse)

# l
students_even = students[::2]
print(students_even)

# m
students_odd = students[1::2]
print(students_odd)