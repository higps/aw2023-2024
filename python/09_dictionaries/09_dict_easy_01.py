# a)
# Create a dictionary with keys "name", "age", and
# "city" and assign it the values "John", 30, and "New
# York".

my_dict = {
    "name": "John",
    "age":  30,
    "city": "New York"
}

# b)
# Extract the value of Johns age from the dictionary in a
# new python variable called age.

age = my_dict["age"]

# c. Add a new key "salary" to the dictionary from the
# previous exercise and assign it the value 50000.
my_dict = {
    "name": "John",
    "age":  30,
    "city": "New York",
    "Salary": 50000
}

# d. Use a for loop to print all the keys in the dictionary
# from the previous exercises.

for key in my_dict:
    print(key)

# e. Use a for loop to print all the values in the dictionary
# from the previous exercises.

for value in my_dict.values():
    print(value)
# f. Use a for loop to print all the keys and their
# corresponding values in the dictionary from the
# previous exercises, in the format "key: value".

for key, value in my_dict.items():
    print("Pairs", key, value)

# g. Create a new dictionary called "my_dict_2" that
# contains the keys and values from "my_dict" from the
# previous exercises, but with the keys and values
# reversed (i.e. the keys from "my_dict" should now be
# the values in "my_dict_2" and vice versa).

def findKey(dictionary, found_value):
    for key, value in dictionary.items():
        print("Key value",key,value)
        if key == found_value:
            return key

my_dict_2 = {
    my_dict["name"]:findKey(my_dict, "name"),
    my_dict["age"]:findKey(my_dict, "age"),
    my_dict["city"]:findKey(my_dict, "city"),
    my_dict["Salary"]:findKey(my_dict, "Salary")
}

for key, value in my_dict_2.items():
    print("Pairs mydict 2", key, value)


my_dict_2v2 = {
    value: key for key, value in my_dict.items()
    }

# h. Create a new dictionary called "my_dict_3" that
# contains the same keys as "my_dict" from the
# previous exercises, but with the values set to 0.

# my_dict_3 = {
#     key for key in my_dict : 0
#     }

my_dict_3v2 = {key: 0 for key in my_dict}


print(my_dict_3v2)

# i. Use the "update" method to merge the contents of
# "my_dict" and "my_dict_2" from the previous
# exercises into a new dictionary called "my_dict_4"

my_dict_4 = {}

my_dict_4.update(my_dict)
my_dict_4.update(my_dict_2)
print(my_dict_4)