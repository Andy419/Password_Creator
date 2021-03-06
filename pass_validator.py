# --------------------------------------
#   Name: Andrew Samoil
#   ID: 1621231
#   CMPUT 274, Fall 2020
#
#   Weekly Exersize 1: Password Validator
# --------------------------------------

from random import randint

# validate() checks to see if the inputed password is Secure,
# Insecure, or Invalid


def validate(password):
    ForbiddenCharacters = {" ", "@", "#"}
    SpecialCharacters = {'!', '-', '$', '%', '&', '\'',
                         '(', ')', '*', ';', ']', '\"',
                         '\\', '+', ',', '.', '/', ':',
                         '<', '=', '>', '?', '_', '[',
                         '^', '`', '{', '|', '}', '~'}
    # loop to check if password contains any invalid characters
    for char in password:
        if char in ForbiddenCharacters:
            return 'Invalid'

    # check if length of passwords is too short (less than 8)
    if len(password) < 8:
        return 'Invalid'

    # check if password contains lower, upper, number and special characters

    # The password must have 1 of all four in order to be condsidered valid
    UpperCount = 0
    LowerCount = 0
    NumCount = 0
    SpecialCount = 0
    for char in password:
        if char.islower():
            LowerCount += 1
        elif char.isupper():
            UpperCount += 1
        elif char.isdigit():
            NumCount += 1
        elif char in SpecialCharacters:
            SpecialCount += 1
    if UpperCount > 0 and LowerCount > 0 and NumCount > 0 and SpecialCount > 0:
        return "Secure"
    else:
        return "Insecure"

# validate will randomly generate a guarenteed Secure password


def generate(n):
    # Insure password will be long enough
    if n < 8:
        return

    # sets of all characters to be used in the password
    SpecialCharacters = ['!', '-', '$', '%', '&', '\'',
                         '\"', '(', ')', '*', '\\', '+',
                         ',', '.', '/', ':', ';', '<',
                         '=', '>', '?', '_', '[', ']',
                         '^', '`', '{', '|', '}', '~']

    UpperCharacters = ['A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    AllCharacters = [1, 2, 3, 4, 5, 6, 7, 8, 0, 'A', 'B',
                     'C', 'D', 'E', 'F', 'G', 'H', 'I', '_',
                     'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                     'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                     'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                     'x', 'y', 'z', '!', '-', '$', '%', '&',
                     '\'', '\"', '(', ')', '*', '\\', '+', ',',
                     '.', '/', ':', ';', '<', '=', '>', '?',
                     '[', ']', '^', '`', '{', '|', '}', '~']
    passwerd = ""

    # Loop combines at least 1 of each valid element to the password
    for i in range(0, 1):
        passwerd += str(SpecialCharacters[randint(0, 28)])
        passwerd += str(UpperCharacters[randint(0, 25)])
        passwerd += str(randint(0, 9))
        passwerd += str(UpperCharacters[randint(0, 25)].lower())

    # The rest of the password is randomly-ish generated by all
    # of the characters via AllCharacters
    n = n - 4
    for i in range(0, n):
        passwerd += str(AllCharacters[randint(0, 89)])
    
    return passwerd

n = 0
for i in range(1000):
    pwd = generate(18)


    if len(pwd) != 18:
        print(pwd)
        n += 1
print(n)
