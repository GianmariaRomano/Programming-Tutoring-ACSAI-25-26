'''
Write a function to order a list of positive integers so that the odd numbers
appear before the even numbers and the odd numbers are in increasing order,
while the even numbers are in decreasing order.

EXAMPLE: [1, 5, 2, 6, 7, 4, 5, 3, 8] -> [1, 3, 5, 7, 8, 6, 4, 2]
'''

def my_key_5(x):
    '''
    Idea: For odd numbers, sort by decreasing modulus and increasing value.
    For even numbers, sort by increasing modulus and decreasing value.
    '''
    if x % 2 == 1:
        return -(x % 2), x
    else:
        return x % 2, -x