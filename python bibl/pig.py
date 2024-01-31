# get sentence from user

original = input("Enter sentence: ").strip().lower()

# split sentence to individual words

words = original.split()
#print(words)

# loop through words and convert to pig latin

new_words = []

#if starts with vowel, just add "yay"
vowel = "aeiou"
for word in words:
    if word[0] in vowel:
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in vowel:
                vowel_pos += +1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
        


# stick words back together

output = " ".join(new_words)

# output the final string

print(output)
