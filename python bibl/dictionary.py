students = {}
students = {"Alice":25,"Bob":27,"Claire":17,"Dan":21,"Emma":22}

print(students["Dan"])


students["Fred"] = 25
print(students["Fred"])

students["Alice"] = 26
print(students["Alice"])

del students["Fred"]

print(students.keys())

a = list(students.keys())

print(a[1], a[0])

print(students.items())
