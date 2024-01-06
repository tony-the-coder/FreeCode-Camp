### Look more into \W and what is special about the _
### As a reminder, practice all() and any() some to get a good grasp
### Find a way to practice generators and for within all()
### Is _ in python just a local variable and why not just use a letter?
### A reminder to go back and double check on __main__ and __name__
#########From just looking at this again with fresh eyes, it looks like the __name__ is talking about the main() function, and it is then you can run the stuff inside it, but I am not sure what FCC means by saying that it will keep it from running when it is imported as a modual. I think that is what I was kind of saying before? More practice would do me good

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ""
        # Generate password
        for _ in range(length):
            ###secrets.choice is supposed to better than random.
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r"\d"),
            (special_chars, rf"[{symbols}]"),
            (uppercase, r"[A-Z]"),
            (lowercase, r"[a-z]"),
        ]

        # Check constraints and look more into all() and any()
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password


if __name__ == "__main__":
    new_password = generate_password()
    print("Generated password:", new_password)
