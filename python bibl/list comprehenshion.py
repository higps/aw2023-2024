even_numbers = [x for x in range(1,101) if x % 2 == 0]
odd_numbers = [x for x in range(1,101) if x % 2 != 0]
print(even_numbers)
print(odd_numbers)



words = ["the", "quick", "brown", "fox", "jumps", "the", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
