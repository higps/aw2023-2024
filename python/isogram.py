def is_isogram(string):
    letter = string.strip().lower()
    read_letter = {}

    for a in letter:

        if a not in read_letter:
            read_letter[a]= [a]
        else:
            return False

    return True

def is_isogram2(string):
    print(set(string.lower))
    print(len(set(string.lower())))
    return len(string) == len(set(string.lower()))


is_isogram2("Hellu")
is_isogram2("Helu")
is_isogram2("Hel")
is_isogram2("Helllllll")