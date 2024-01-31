num = {
"numbers": [1,2,3]
}

# print(num["numbers"])



def sum_nums(nums):
    sum_num = 0
    for num in nums:
        sum_num += num
    return sum_num

print(num.keys())
# print(sum_nums(num.values()))

for value in num.values():
    print(value)