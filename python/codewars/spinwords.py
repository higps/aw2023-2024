def spin_words(sentence):
    words = sentence.split()
    new_sentence = []
    
    for word in words:
        if len(word) >= 5:
            new_sentence.append(word[::-1])
        else:
            new_sentence.append(word)
    return " ".join(new_sentence)


print(spin_words("Hey fellow warriors"))# => returns "Hey wollef sroirraw" 
spin_words("This is a test")# => returns "This is a test" 
spin_words( "This is another test")#=> returns "This is rehtona test"