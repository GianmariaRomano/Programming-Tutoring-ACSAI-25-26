'''
Write a function that sorts a list of strings, considering the number of
characters in increasing order, then the ending letter and finally the
lexicographical order.

EXAMPLE: ["snake", "caterpillar", "rat", "bat", "dog"] -> ["dog", "bat", "rat", "snake", "caterpillar"]
'''

def my_key_3(x):
    return len(x), x[-1], x