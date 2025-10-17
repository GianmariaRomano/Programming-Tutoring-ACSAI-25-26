'''
Write a function that takes an input list and
returns True if the list is sorted in ascending
or descending order, or False otherwise.
HINT: Be careful about duplicates.
      Use a single loop and do not use sort()/sorted().
'''

def sorted_list(l):
    if len(l) == 1:
        return True
    direction = "X" # "X" = Unknown order, "A" = Ascending order, "D" = Descending order.
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            if direction == "D":
                return False
            direction = "A"
        if l[i] < l[i - 1]:
            if direction == "A":
                return False
            direction = "D"
        return True