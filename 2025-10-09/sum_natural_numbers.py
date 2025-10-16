'''
Exercise: Sum of First N Natural Numbers with Separate Calculation and Printing Functions
The sum of the first n natural numbers (1 + 2 + 3 + ... + n) 
can be calculated using the formula: sum = n * (n + 1) / 2.

Define a function called calculate_sum_natural_numbers.
The function should:
- Take an integer parameter n.
- Use a for loop with range() to sum the numbers from 1 to n.
- Return the final sum.

Define a function called sum_natural_numbers.
The function should:
- Take an integer parameter n.
- Call calculate_sum_natural_numbers and return the sum.

Define a function called print_sum.
The function should:
- Take two parameters: n and the sum.
- Print the sum and mention the formula for verification.

Call sum_natural_numbers with a sample value (e.g., 5),
then call print_sum with the result.
'''

def calculate_sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_natural_numbers(n):
    s = calculate_sum_natural_numbers(n)
    return s

def print_sum(n, total_sum):
    print(f"Sum of the first {n} natural numbers: n * (n + 1) / 2 = {total_sum}")

# Example call.
total = sum_natural_numbers(5)
print_sum(5, total)