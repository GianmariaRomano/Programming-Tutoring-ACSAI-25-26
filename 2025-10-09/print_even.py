'''
Exercise: Print Even Numbers
Define a function called print_even_numbers.
The function should:
- Take two integer parameters: start and end.
- Use a for loop and range() to iterate from start to end (inclusive).
- For each number in the range, use an if statement to check if the number is even.
- If the number is even, print it.

Call print_even_numbers with sample values (e.g., 1 and 10).
'''

def print_even_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)

# Example call.
print_even_numbers(1, 10)