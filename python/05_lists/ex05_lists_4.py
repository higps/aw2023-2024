# Create the following variable:
# list_of_lists = [1, [2, 3,”4”], [5, [6, ”7”, 8], 9, 10]]
# use list selection and change the string values to numbers,
# hence “4” to 4 and “7” to 7.

list_of_lists = [1, [2, 3,"4"], [5, [6, "7", 8], 9, 10]]

#list_of_lists[1][2] = 4

#print(list_of_lists)

#ist_of_lists[2][1][1] = 7

#print(list_of_lists)

list1 = list_of_lists[1]

print(list1)
list1[-1] = 4

print(list_of_lists)