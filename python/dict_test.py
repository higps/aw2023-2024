list1 = ["a","b","c"]
dict2 = {"John":list1}
dict3 = {"Person":dict2}

for values in dict3.values():
    for i in values.values():
        
        empty_list = []
        for k in i:
            empty_list.append("f")
        list1 = empty_list
        # dict2 = {dict2.keys:empty_list}

print(list1)
print(dict2)


# print(dict2.items())

# for i,j in dict2.items():

#     for k in j:
#         print(k)

# for j in dict2.values():
#     print(j)
#     # for k in j:
#     #     print(k)
