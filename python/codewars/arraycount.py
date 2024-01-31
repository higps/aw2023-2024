def highest_rank(arr):
    dict = {}
    print(arr)
    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    
    highest = 0
    highest_key = 'null'
    for key, val in dict.items():
        if val > highest:
            highest = val
            highest_key = key
        elif val == highest:
            if key > highest_key:
                highest_key = key
    return highest_key

highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12])
highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10])