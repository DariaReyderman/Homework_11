text1 = " fun-day "
print('a', "without strip:", text1)
print(' ', "with strip:", text1.strip())

print('b', "isalpha:", "hello".isalpha())
print('c', "isdigit:", "777".isdigit())
print('d', "isspace:", "   ".isspace())
print('e', "join:", "".join(['N', 'I', 'N', 'J', 'A']))
print('f', "join:", "*".join(['N', 'I', 'N', 'J', 'A']))
print('g', "in, lower:", "e" in "hELLo".lower())

# Bonus
word: str = input("Enter a word: ")
letters = [letter.upper() for letter in word if letter.isalpha()]
print(letters)
