def DNA_strand(dna):

    letter_list = list(dna)
    print(letter_list)
    
    return_value = []
    for letter in letter_list:
        new_letter = letter.replace('T','A').replace('A','T').replace('G','C').replace('C','G')
        print(new_letter)
        return_value.append(new_letter)

    #new_string = dna.replace('T','A').replace('A','T')
    print(return_value)


#DNA_strand("ATTGC")
DNA_strand("GTAT")
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"