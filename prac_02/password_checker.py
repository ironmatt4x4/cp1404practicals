"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    pass_length = len(password)
    if MIN_LENGTH < pass_length > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for i in range(0, pass_length, 1):
        test_lower = password[i].islower()
        if test_lower is True:
            count_lower += 1

        test_upper = password[i].isupper()
        if test_upper is True:
            count_upper += 1

        test_digit = password[i].isdigit()
        if test_digit is True:
            count_digit += 1

        if password[i] in SPECIAL_CHARACTERS:
            count_special += 1

        pass

    if count_lower == 0:
        return False
    elif count_upper == 0:
        return False
    elif count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED is True:
        if count_special < 1:
            return False

    return True


main()
