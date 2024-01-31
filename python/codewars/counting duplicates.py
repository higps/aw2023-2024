def duplicate_count(text):
    duplicates = 0
    new_dict = {}
    text_string = text.lower()
    for i in text_string:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for v in new_dict.values():
        if v > 1:
            duplicates += 1
    
    return duplicates

print(duplicate_count("ABBBA"))