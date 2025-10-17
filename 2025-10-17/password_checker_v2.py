'''
Write a function that checks the validity of a password.
The password must:
- Contain at least one letter among [a-z] and a letter among [A-Z]
- Contain at least one number between [0-9]
- Contain at least one character among [$#@]
- Be at least 6 characters long and not more than 16 characters long
- The password is not valid if it contains different characters from the ones mentioned above
  or if it violates one of the specified rules
The function outputs True/False based on whether the password is valid or not.
'''

def is_uppercase(char):
    # Hint: Exploit ord("A") = 65 and ord("Z") = 90.
    return (65 <= ord(char) <= 90)

def is_lowercase(char):
    # Hint: Exploit ord("a") = 97 and ord("Z") = 122.
    return (97 <= ord(char) <= 122)

def is_digit(char):
    # Hint: Exploit ord("0") = 48 and ord("9") = 57.
    return (48 <= ord(char) <= 57)

def is_special(char):
    return char == "$" or char == "#" or char == "@"

def password_checker_v2(pwd):
    if len(pwd) < 6 or len(pwd) > 16:
        return False
    upper = False
    lower = False
    digit = False
    special = False
    for c in pwd:
        if is_uppercase(c):
            upper = True
        elif is_lowercase(c):
            lower = True
        elif is_digit(c):
            digit = True
        elif is_special(c):
            special = True
        else:
            return False
    return lower and upper and digit and special