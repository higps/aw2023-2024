current_number=50
total_numb=100
bar_length=10

load_length = int(current_number/total_numb*bar_length)
remaining_length = int((total_numb-current_number)/total_numb*bar_length)

load_bar = '=' * load_length
remaining_bar = ' ' * remaining_length

print(f'|{load_bar}>{remaining_bar}|')