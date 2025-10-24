'''
Given an increasingly sorted integer array, remove the duplicate elements
in place and return the number of unique elements remaining in the array.
Hint: Assuming the list contains k unique elements, change the array in
      such a way that the first k elements are the unique values.
'''

def remove_duplicates(nums):
    unique_items = 1 # The list always guaranteed to contain at least one unique element.
    for i in range(len(nums)):
        if nums[i] != nums[unique_items - 1]:
            nums[unique_items] = nums[i]
            unique_items += 1
    return unique_items