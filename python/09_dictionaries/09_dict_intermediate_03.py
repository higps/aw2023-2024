# 3. Write a Python script to concatenate following dictionaries
# to create a new one

# a. Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6:
# 60}
dict = {}

def concat_dict(dic1, dic2, dic3):

    dict = {**dic1, **dic2, **dic3}
    print(dict)

concat_dict(dic1,dic2,dic3)

# b. Write a function called “unfold_dict” that takes a
# single dictionary as input. And return an unfolded
# version of the dictionary
# example:

def unfold(i_dict):
    for key1 in i_dict.keys():
        sub_dict = i_dict[key1]
        for key2 in sub_dict.keys():
            value = sub_dict[key2]
            new_key = key1+key2
            dict_unfold[new_key] = value
    return dict_unfold
    

input_dict = {
 "a":{"d":1, "e":2},
 "b":{"f":3},
 "c":{"g":4, "h":5}
}

input_dict2 = {
 "a":{"d":1, "e":2},
 "b":{"f":3},
 "c":{"g":4, "h":5},
 "i":{"f":6}
}
# Expected Result : {"ad":1, "ae":2, "bf":3, "cg":4, "ch":5}
dict_list = [input_dict, input_dict2]

for dicts in dict_list:
    unfold

dict_unfold = {}

def unfold(i_dict):
    for key1 in i_dict.keys():
        sub_dict = i_dict[key1]
        for key2 in sub_dict.keys():
            value = sub_dict[key2]
            new_key = key1+key2
            dict_unfold[new_key] = value
    return dict_unfold
    

print(dict_unfold)