'''
Define a function generate_power_set(nums) that generates the powerset of a list
as a list containing all possible subsets/sublists of the list, including the
empty set and the list itself.
'''

def generate_power_set(nums):
    power_set = [[]] # Start by initializing the powerset with just the empty list.
    for n in nums:
        all_elements = []
        for s in power_set:
            list_s = s.copy()
            list_s.append(n)
            all_elements.append(list_s)
    return power_set