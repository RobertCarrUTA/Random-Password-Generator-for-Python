import random
import string

print('0. Lowercase letters')

print('Please select from the above list the character types of your password: ')

choice = int(input())

print('Please enter a password length in the range of 8-256')

length = int(input())

if (choice == 0):
    print(''.join(random.choices(string.ascii_lowercase, k = length)))
