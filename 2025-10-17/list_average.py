'''
Write a function that, given a list containing non-negative values,
creates a new list containing only the elements of the original list
that satisfy the following property:
    my_list[i] > 2 * average(my_list[0:i])
The first element is therefore never inserted.
For instance, consider the list [5, 3, 10, 0]:
- The first element is 5, which is never inserted.
- The second element is 3: the average of the elements in [0, 0] is 5, so 3 < 2 * 5 is not inserted.
- The third element is 10: the average of the elements in [0, 1] is 4, so 10 > 2 * 4 is inserted.
- The third element is 0: the average of the elements in [0, 2] is 6, so 0 < 2 * 6 is not inserted.
'''

def list_average(l):
    s = []
    for i in range(1, len(l)):
        avg = average(l[0:i])
        if l[i] > 2 * avg:
            s.append(l[i])
    return s

def average(l):
    return sum(l) / len(l)