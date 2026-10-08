'''
On paper, write a program that asks the user for a password,
with error-checking to repeat if the password doesn't meet a minimum length set by a CONSTANT.

The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.

'''


def main():
    MINIMUM_LENGTH = 5

    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Password")
        password = input("Password: ")
    print_astricks(password)


def print_astricks(password):
    for letter in password:
        print("*", end=" ")


main()
