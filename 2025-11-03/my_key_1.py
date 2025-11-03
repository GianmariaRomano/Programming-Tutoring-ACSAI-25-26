'''
Write a function that sorts a list of strings ignoring the case and
then in lexicographical order.

EXAMPLE: ["bar", "cat", "Cat", "car"] -> ["bar", "car", "Cat", "cat"]
'''

def my_key_1(x):
    return x.lower(), x