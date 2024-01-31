# 1 Create convert function. Convert miles to km
def convert_miles_to_km(x):
    return x * 1.60934

km = convert_miles_to_km(100)
km2 = convert_miles_to_km(160)

print(km)
print(km2)

# 2 Add another function called ‘get_nth_word’, the function should have two inputs. A text and a number. It should show the full text in terminal, and return the n’th word.

def get_nth_word(word, x):
    print(word)
    word_split = word.split()
    return word_split[x]

get_nth_word("hello beautiful world",2)

# 3 Create a new function called ‘get_indexes’. The function should take two arguments, a list and a value and then return a list of all indexes where the list matches the value. If no value matches, the function should return an empty list [ ]

def get_indexes(x, y):
    # Make sure x is a list
    if not isinstance(x, list):
        raise ValueError("x must be a list")
    
    # Create the return table
    matches = []
    # Use the range of length of x to be able to iterate over the words
    for i in range(len(x)):
        if x[i] == y:
            matches.append(i)

    return matches

world_index = get_indexes(["hello", "beautiful", "world"], "world")
something_index = get_indexes(["hello", "beautiful", "world"], "something")
seven_index = get_indexes([5, 7, 72, 7, 14, 7, 26], 7)

print(world_index)
print(something_index)
print(seven_index)