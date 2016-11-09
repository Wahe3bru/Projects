#Check if Palindrome - Checks if the string entered by the user is a palindrome.
#That is that it reads the same forwards as backwards like “racecar”

test = input('please enter possible palindrome ')
tset = ''.join(reversed(test))

if test == tset:
    print("your word is a palindrome")
else:
    print("your word is not a palindrome; " + tset)
