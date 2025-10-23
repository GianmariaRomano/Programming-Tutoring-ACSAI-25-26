'''
Write functions to manipulate a tuple containing multiple data types.

Your program should:
- Create a tuple with five elements: three integers, a string, and a list.
- Retrieve and print the length of the tuple.
- Access and print each element by its index.
- Reverse the tuple using slicing and return the reversed tuple.
- Modify the list element inside the tuple by appending a new item (this modification should be done in place; no return value needed).

Functions:
- create_tuple(): Returns the initial tuple with mixed data types.
- get_tuple_length(t): Takes a tuple and returns its length.
- access_element(t, index): Takes a tuple and an index, returns the element at that index.
- reverse_tuple(t): Takes a tuple and returns a reversed tuple using slicing.
- modify_list_in_tuple(t, new_item): Takes the tuple and a new item, appends the item to the list element inside the tuple in place.

Example usage:
    >>> t = create_tuple()
    >>> get_tuple_length(t)
    5
    >>> access_element(t, 3)
    'hello'
    >>> reverse_tuple(t)
    ([1, 2, 3], 'hello', 30, 20, 10)
    >>> modify_list_in_tuple(t, 4)
    >>> t[-1]
    [1, 2, 3, 4]
'''

def create_tuple():
    # Harder way: users can enter the values they want.
    ints = []
    for i in range(3):
        n = int(input("Enter an integer value: "))
        ints.append(n)
    text = input("Enter a string: ")
    input_int_list = input("Enter a list of integers separated by a comma: ")
    int_list = [int(i) for i in input_int_list.split(",")]
    return (ints[0], ints[1], ints[2], text, int_list)

def get_tuple_length(t):
    return len(t)

def access_element(t, index):
    # For simplicity, assume that index is always within the bounds of t.
    if -len(t) <= index < len(t):
        return t[index]

def reverse_tuple(t):
    return t[::-1]

def modify_list_in_tuple(t, new_item):
    # Assume for simplicity that the list is always at the end of the tuple.
    l = access_element(t, -1)
    l.append(new_item)