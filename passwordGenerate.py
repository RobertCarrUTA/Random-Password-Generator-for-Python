import random
import string
import sys

list = """
0. Lowercase letters
1. Uppercase letters
2. Lowercase and Uppercase letters
3. Digits
4. Special Symbols (!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
5. Generate Password using letters, digits, and special characters
"""

print(list)
print('Please select from the above list the character types of your password:')

choice = int(input())

print('Please enter a password length in the range of 8-256:')

length = int(input())

# Perform a sys.exit() if the length is outside of the accepted boundaries
if (length < 8 or length > 256):
    print('Error: The length must be between the values of 8-256. The program will now exit.')
    sys.exit()

print('\nYour password is:')

if (choice == 0):
    print(''.join(random.choices(string.ascii_lowercase, k = length)))
elif (choice == 1):
    print(''.join(random.choices(string.ascii_uppercase, k = length)))
elif (choice == 2):
    print(''.join(random.choices(string.ascii_letters, k = length)))
elif (choice == 3):
    print(''.join(random.choices(string.digits, k = length)))
elif (choice == 4):
    print(''.join(random.choices(string.punctuation, k = length)))
elif (choice == 5):
    print(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = length)))