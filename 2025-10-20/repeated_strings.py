'''
Write functions to concatenate strings according to repetition counts using subfunctions.

- repeat_string(s, n): repeat string s, n times.
- repeat_all_strings(strings, counts): repeat each string in the list by the corresponding count.
- concatenate_strings(strings): concatenate a list of strings into a single string.
- concatenate_repeated_strings(strings, counts): main function that uses the above to return the concatenated repeated string.

Example:
If strings = ['ab', 'o o'] and counts = [2, 3], concatenate_repeated_strings returns 'ababo oo oo o'.

Functions:
- repeat_string(s, n): Takes a string (s) and positive integer (n), returns s repeated n times.
- repeat_all_strings(strings, counts): Takes lists of strings and integers, returns list with each string repeated.
- concatenate_strings(strings): Takes list of strings, returns concatenated string.
- concatenate_repeated_strings(strings, counts): Uses above functions to produce final concatenated string.

Example usage:
>>> concatenate_repeated_strings(['ab', 'o o'], [2, 3])
'ababo oo oo o'
'''

def repeat_string(s, n):
    return s * n

def repeat_all_strings(strings, counts):
    # Assume for simplicity that strings and counts have the same length.
    return [repeat_string(strings[i], counts[i]) for i in range(len(strings))]

def concatenate_strings(strings):
    return "".join(strings)

def concatenate_repeated_strings(strings, counts):
    words = repeat_all_strings(strings, counts)
    concatenated_words = concatenate_strings(words)
    return concatenated_words
