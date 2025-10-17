'''
Given a list of integers, each between 0 and 99, write a
function that returns a list of tuples (x, y),
where x is an integer and y is he number of times this
integer appears in the original list.
BONUS: The list of tuples must be sorted based on the first element.
       For instance, the list [5, 4, 1, 4] returns the list [(1, 1), (4, 2), (5, 1)].
'''

def frequency(l):
    tuples = []
    digits = set(l) # Use a set to remove duplicates.
    for digit in digits:
        tuples.append((digit, l.count(digit)))
    sorted_tuples = sort_first_element(tuples)
    return sorted_tuples

def sort_first_element(l):
    return sorted(l, key=lambda x: x[0])