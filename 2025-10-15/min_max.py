'''
Write functions to repeatedly ask the user for integers and keep track of the largest and smallest numbers entered.
The process should continue until the user enters 'done'. At the end, print the largest and smallest numbers.

Functions:
- get_number_input: Ask the user to enter an integer or 'done' to finish. Return the integer or None if 'done' is entered.
- update_largest: Take the current largest value and a new number, and return the updated largest value.
- update_smallest: Take the current smallest value and a new number, and return the updated smallest value.
- min_max_tracker: Use a while loop to repeatedly ask the user for numbers, updating the largest and smallest values, until 'done' is entered. Print the results at the end.
'''

def get_number_input():
    n = input("Insert a number or done to finish: ")
    if n == "done":
        return None
    return int(n)

def update_largest(current_largest, new_number):
    return max(current_largest, new_number)

def update_smallest(current_smallest, new_number):
    return min(current_smallest, new_number)

def min_max_tracker():
    # Start by taking a first number to keep track of maximum and minimum, then loop until "done" is entered.
    first = get_number_input()
    if first == None:
        print("No number has been inserted")
    m = M = first
    # Use an infinite loop that breaks upon typing "done".
    while True:
        n = get_number_input()
        m = update_smallest(m, n)
        M = update_largest(M, n)
    print(f"Minimum value: {m}")
    print(f"Maximum value: {M}")