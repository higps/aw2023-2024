def order(sentence):
    new_sentence = sentence.split()
    sorted_words = []
    x = 1
    while len(sorted_words) < len(new_sentence):
        for word in new_sentence:
            #print(word)
            if str(x) in word:
                # print(f"Appending {word}")
                sorted_words.append(word)
                x += 1
                # print(f"Not Appending {word}")
                # continue
                
    return " ".join(sorted_words)

print(order("is2 Thi1s T4est 3a"))#"Thi1s is2 3a T4est"

def order_2(sentence):
  return " ".join(sorted(sentence.split(), key=min))

