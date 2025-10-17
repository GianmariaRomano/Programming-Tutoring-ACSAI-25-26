'''
Write a function that computes the intersection between two lists.
Given two lists, return a new list containing only the
elements that re present in both lists.
'''

# Simple approach using loops.
def intersect(a, b):
    l = []
    for el in a:
        if el in b:
            l.append(el)
    return el

# Faster approach using list comprehension.
def intersect_v2(a, b):
    return [el for el in a if el in b]

'''
N.B.: Both implementations are symmetric, meaning that one
      can also iterate through b and check whether each
      element also appears in a.
'''