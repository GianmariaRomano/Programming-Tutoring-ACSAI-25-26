'''
Write functions to process a list of strings entered by the user. The user should enter the strings as a single line, separated by spaces.
Your program should:
- Print each string reversed.
- Print each string with digits removed.
- Concatenate all the strings into a single long string without any spaces, then print this string.
- Print the concatenated string as a list of its individual characters.

Example:
Input string: hello 123abc banana

Output:
Reversed strings: ['olleh', 'cba321', 'ananab']
Strings with digits removed: ['hello', 'abc', 'banana']
Concatenated (no spaces): hello123abcbanana
Concatenated string as list: ['h', 'e', 'l', 'l', 'o', '1', '2', '3', 'a', 'b', 'c', 'b', 'a', 'n', 'a', 'n', 'a']

Functions:
- get_strings_input: Ask the user to enter a string of words separated by spaces. Return the corresponding list of strings.
- reverse_strings: Take a list of strings and return a new list with each string reversed.
- remove_digits: Take a list of strings and return a new list with digits removed from each string.
- concatenate_strings: Take a list of strings and return a single concatenated string without spaces.
- string_to_char_list: Take a string and return a list of its individual characters.
- string_list_processor: Use these functions to ask for input, perform the operations, and print the results.
'''

def get_strings_input():
    words = input("Insert some words: ")
    return words.split(" ")

def reverse_strings(strings):
    return [s[::-1] for s in strings]

def remove_digits(strings):
    # Hint: Exploit the fact that ord("0") = 48 and ord("9") = 57.
    no_digits = []
    for string in strings:
        chars = [c for c in list(string) if not(48 <= ord(c) <= 57)]
        word = "".join(chars)
        no_digits.append(word)
    return no_digits

def concatenate_strings(strings):
    return "".join(strings)

def string_to_char_list(s):
    return list(s)

def string_list_processor():
    my_words = get_strings_input()
    reversed_strings = reverse_strings(my_words)
    for gnirts in reversed_strings:
        print(gnirts)
    no_nrs = remove_digits(my_words)
    for string in no_nrs:
        print(string)
    mywords = concatenate_strings(my_words)
    print(mywords)
    mychars = string_to_char_list(mywords)
    print(mychars)
