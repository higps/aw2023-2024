def array_diff(a, b):
    diff = []
    for i in a:
        if i not in b:
            diff.append(i)
    return diff


print(array_diff([1,2],[1]))