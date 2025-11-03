'''
Write a function that sorts a list of strings considering the number of vowels
in decreasing order, then the whole length in increasing order and finally the
reverse alphabetical order.

EXAMPLE: ["pear", "peach", "apple", "banana", "avocado"] -> ["avocado", "banana", "pear", "apple", "peach"]
'''

'''
Here, the game gets complicated because it is not possible to suse the -x command.
For this reason, it is more convenient to create a function that works in the
other way around and then specify reverse=True in the sorted() function.
'''

def my_key_4(x):
    return sum([x.count(i) for i in "aeiou"]), -len(x), x