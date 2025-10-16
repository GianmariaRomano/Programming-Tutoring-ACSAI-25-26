'''
Exercise: Advanced Password Format Checker (with subfunctions)
Define the following subfunctions:
- is_uppercase(char): returns True if char is an uppercase letter (A-Z, use ord()).
- is_lowercase(char): returns True if char is a lowercase letter (a-z, use ord()).
- is_digit(char): returns True if char is a digit (0-9, use ord()).

Define the function password_checker.
The function should:
- Take a string parameter called password.
- Check if the password is exactly 8 characters long.
- Use the subfunctions and if statements to verify:
- The first character is uppercase.
- The next three characters are lowercase.
- The last four characters are digits.
- Return True if all conditions are met, otherwise return False.

Define a function called print_password_check.
The function should:
- Take a string parameter.
- Call password_checker and print:
  "Valid password format" if True, "Invalid password format" if False.

Call print_password_check with a sample string (e.g., "Abcd1234").
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

def password_checker(password):
    if len(password) != 8:
        return False
    if not(is_uppercase(password[0])):
        return False
    for char in password[1:4]:
        if not(is_lowecase(char)):
            return False
    for digit in password[4:]:
        if not(is_digit(digit)):
            return False
    return True

def print_password_check(password):
    if password_checker(password):
        print("Valid password format")
    else:
        print("Invalud password format")

# Example call.
print_password_check("Abcd1234") # True