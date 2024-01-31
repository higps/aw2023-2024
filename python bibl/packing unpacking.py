#* tuples , iterables

def add(*numbers):
    total = 0
    for number in numbers:
            total += number
    return total

print (add(1,2,3,4,5,6,7,8,9))


def about(name, age, likes):
    sentence = f"Meet {name} age {age} likes {likes}"
    return sentence

dictionary = {"name": "Marius", "age":23, "likes": "Python"}
print(about(**dictionary))

#** dictionary
def foo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

foo(huda = "Female", marius = "Male")
