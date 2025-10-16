'''
Exercise: Calculate Sum and Average
Define a function called calculate_sum_and_average.
The function should:
- Take three numerical parameters: num1, num2, and num3.
- Calculate the sum of the three numbers.
- Calculate the average of the three numbers.
- Return both the sum and the average as a tuple.

Define a function called print_sum_and_average.
The function should:
- Take three numbers as parameters.
- Call calculate_sum_and_average to get the sum and average.
- Print the messages:
  "Sum: {sum}"
  "Average: {average}"

Call print_sum_and_average with sample values (e.g., 10, 20, 30).
'''

def calculate_sum_and_average(num1, num2, num3):
    s = num1 + num2 + num3
    a = s / 3
    return (s, a)

def print_sum_and_average(num1, num2, num3):
    s, a = calculate_sum_and_average(num1, num2, num3) # Assign both variables using a tuple.
    print(f"Sum: {s}")
    print(f"Average: {a}")

# Example call.
print_sum_and_average(10, 20, 30)