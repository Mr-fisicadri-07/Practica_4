'''
A simple password generator that creates a random password of a specified length.

Args:
    length (int): The desired length of the password.

Returns:
    str: A randomly generated password.

Example:
    >>> generate_password(12)
    'aB3$dEf9Gh!2'
'''

import random

length = int(input("\nEnter the desired length of the password: "))

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("\nGenerated password: {}\n".format(generate_password(length=length)))