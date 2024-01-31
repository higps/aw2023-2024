# Create a new python program and check if a string is a palindrome (is the
# same forward and backwards e.g. maddam)

def ispalindrome(string):
    if string == string[::-1]:
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not palindrome")
        


the_string = "maddam"
ispalindrome(the_string)
