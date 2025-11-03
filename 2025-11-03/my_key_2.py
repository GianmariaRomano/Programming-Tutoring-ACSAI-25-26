'''
Write a function that sorts a list of tuples of three positive integers
considering the second element, then the first element and finally the
third element.

EXAMPLE: [(1, 5, 6), (3, 4, 9), (1, 1, 1)] -> [(1, 1, 1), (3, 4, 9), (1, 5, 6)]
'''

def my_key_2(x):
    return x[1], x[0], x[2]