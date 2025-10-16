'''
Write functions to repeatedly ask the user for a string and perform advanced slicing and manipulation operations.
The process should continue until the user enters 'done' as the string.

For each string the program should print:

Example:
Input string: programming

Output:
Reversed string: gnimmargorp
String with odd ASCII chars removed: prrn
String with first and last three characters swapped: inggrammpro

Functions:
- get_string_input: Ask the user to enter a string or 'done' to finish. Return the string or None if 'done' is entered.
- reverse_string: Take a string and return its reverse using slicing.
- remove_odd_ascii_chars: Take a string and return a new string with all characters removed whose ASCII code is odd.
- swap_first_last_three: Take a string and return a new string with the first and last three characters swapped (if possible), otherwise return the original string.
- string_manipulator: Use a while loop to repeatedly ask the user for a string, perform the above operations, and print the results. Stop when 'done' is entered.
'''

def get_string_input():
    string = input("Enter a word or done to finish: ")
    if string == "done":
        return None
    return string

def reverse_string(s):
    return s[::-1]

def remove_odd_ascii_chars(s):
    s_even = ""
    for char in s:
        if ord(char) % 2 == 0:
            s_even += char
    return s_even

def swap_first_last_three(s):
    if len(s) < 6:
        return s
    return s[-3:] + s[3:-3] + s[:3]

def string_manipulator():
    # Use an infinite loop that breaks upon typing "done".
    while True:
        word = get_string_input()
        if word == None:
            break
        drow = reverse_string(word)
        wrd = remove_odd_ascii_chars(word)
        rdwo = swap_first_last_three(word)
        print(drow)
        print(wrd)
        print(rdwo)
