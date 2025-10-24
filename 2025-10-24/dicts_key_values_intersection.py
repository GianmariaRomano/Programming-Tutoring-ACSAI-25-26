'''
Define a function dicts_key_values_intersection(dictionaries_list) that takes a
list of disctionaries as input and returns a new dictionary representing the
intersection of the keys and their associated integer lists across all dictionaries.
'''

def dicts_key_values_intersection(dictionaries_list):
    all_keys = [d.keys() for d in dictionaries_list]
    common_keys = set.intersection(*(set(k) for k in all_keys)) # The *() command is used to unpack the comprehension into individual items.
    intersection_dict = {}
    for k in common_keys:
        k_values = [d[k] for d in dictionaries_list if k in d.keys()]
        common_values = set.intersection(*(set(v) for v in k_values))
        intersection_dict[k] = list(common_values) # Insert the (k, v) pair representing the intersection.
    return intersection_dict