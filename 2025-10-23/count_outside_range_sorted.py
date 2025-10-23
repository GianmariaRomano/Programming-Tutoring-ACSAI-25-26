'''
Write functions to count occurrences of integers outside a specified range in a list and return a sorted dictionary.

The program should:

- Take as input a list of integers and two integers m and n defining an inclusive range [m, n].
- Return a dictionary with keys as integers from the list that are NOT in the range [m, n], and values as the count of their occurrences.
- The returned dictionary must be sorted by keys in ascending order.

Example:  
Input: int_list = [4, 4, 10, 4, 2, 1, 2, 15], m = 3, n = 10  
Output: {1: 1, 15: 1}

Functions:

- is_outside_range(num, m, n): Takes an integer num and range bounds m, n, returns True if num is not in [m, n].
- update_frequency(freq_dict, num): Updates the count of num in the dictionary freq_dict.
- sort_dict_by_keys(d): Takes a dictionary and returns a new dictionary sorted by keys.
- count_and_sort_outside_range(int_list, m, n): Processes int_list, uses the above functions, and returns the sorted frequency dictionary.

Example usage:  
>>> count_and_sort_outside_range([4, 4, 10, 4, 2, 1, 2, 15], 3, 10)  
{1: 1, 15: 1}
'''

def is_outside_range(num, m, n):
    return (num < m) or (num > n)

def update_frequency(freq_dict, num):
    freq_dict[num] = freq_dict.get(num, 0) + 1 # Using .get(num, 0) sets the value to 0 if the key is not present.

def sort_dict_by_keys(d):
    d_sorted = {i:d[i] for i in sorted(d.keys())}
    return d_sorted

def count_and_sort_outside_range(int_list, m, n):
    d = {}
    for i in int_list:
        if is_outside_range(i, m, n):
            update_frequency(d, i)
    d_sorted = sort_dict_by_keys(d)
    return d_sorted
