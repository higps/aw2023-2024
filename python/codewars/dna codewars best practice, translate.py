import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))