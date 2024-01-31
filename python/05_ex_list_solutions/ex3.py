# a
values = [4,8,6,2,45,7,98,0,15,3,5,7,8,3,65,8,4,3,5,764,4,3,6]
alpha = 0.1

# b
values_sort = sorted(values)

# c
n = len(values)
lower_idx = round(n*alpha/2)
upper_idx = round(n*(1-alpha/2))-1

# d
print(f'{(1-alpha)*100}% of values are between {values_sort[lower_idx]} and {values_sort[upper_idx]}')

