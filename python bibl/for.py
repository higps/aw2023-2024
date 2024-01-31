#range(1,11)

#for number in range(1,11):
   # print(number)

#for letter in "ABCD":
  #  print(letter)
#for number in range(1,11,2):
 #   print(number)


vowels = 0
consonants = 0
word = "Supercalifragilisticexpialidocius"

for letter in word:
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter == " ":
        pass
    else:
        consonants += 1

print(f"{word} had {vowels} vowels and {consonants} consonants")
