def DNA_strand(dna):
    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    return_value = [complement_dict[letter] for letter in dna]
    
    return ''.join(return_value)

# Example usage:
result = DNA_strand("ATTGC")
print(result)  # Output: TAACG

result = DNA_strand("GTAT")
print(result)  # Output: CATA