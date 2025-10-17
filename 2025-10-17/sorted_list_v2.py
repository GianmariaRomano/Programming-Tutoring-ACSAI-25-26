'''
Write a function that checks whether a list of integers
is composed by a first parted sorted in increasing order, followed
by another part sorted in descending order (or viceversa).
The two parts do not need to have the same length.
HINT: Use a single loop and do not use sort()/sorted() or the
      sorted_list() defined before.
      For simplicity, assume that the list always has at least three elements.
'''

def is_sorted_half(l):
    peak_found = False
    for i in range(1, len(a) - 1):
        if (a[i] > a[i - 1]) and (a[i] > a[i + 1]):
            if peak_found:
                return False
            peak_found = True
        if (a[i] < a[i - 1]) and (a[i] < a[i + 1]):
            if peak_found:
                return False
            peak_found = True           
    return peak_found