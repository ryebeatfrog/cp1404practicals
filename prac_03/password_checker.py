"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started

the minimum and maximum length of the password
whether a special character is required (note the Boolean naming)
the special characters (as a string; a list is not necessary)

"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    digit_count = len(password)
    if digit_count < MIN_LENGTH or digit_count > MAX_LENGTH:
        return False
        print("Invalid Password length")
    # TODO: if length is wrong, return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    # for character in password:
    # number_of_digit = password.isdigit()
    # number_of_upper = password.isupper()
    # number_of_lower = password.islower()
    # print(password)
    # print(f"Number of lowercase letters: {number_of_lower}")
    # print(f"Number of uppercase letters: {number_of_upper}")
    # print(f"Number of digits: {number_of_digit}")

    for character in password:
        if character.isdigit():
            number_of_digit += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.islower():
            number_of_lower += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1
        # TODO: count each kind of character (use str methods like isdigit)

    # TODO: if any of the 'normal' counts are zero, return False
    if number_of_digit == 0 or number_of_upper == 0 or number_of_lower == 0:
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if IS_SPECIAL_CHARACTER_REQUIRED == True and number_of_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()