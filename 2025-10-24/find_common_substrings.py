'''
Define a function find_common_substrings(word1, word2) that takes two strings as input
and returns a list of substrings common to both strings.
The returned list must not contain duplicates and must be ordered in lexicographical order.
'''

def substrings(word):
    l = []
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            l.append(word[i:j])
    return l

def sort_strings(strings):
    strings.sort()
    return strings

def find_common_substrings(word1, word2):
    substrings_1 = substrings(word_1)
    substrings_2 = substrings(word_2)
    common_substrings = list(set([s for s in substrings_1 if s in substrings_2]))
    sorted_common = sort_strings(common_substrings)
    return sorted_common
