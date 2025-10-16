'''
Exercise: Simple Interest Calculator
Define a function called calculate_simple_interest.
The function should:
- Take three parameters: principal (float), rate (float), and time (float).
- Calculate the simple interest using the formula: Interest = (Principal * Rate * Time) / 100.
- Return the calculated interest.

Define a function called print_interest.
The function should:
- Take principal, rate, and time as parameters.
- Call calculate_simple_interest to get the interest value.
- Print the message: "The interest for a principal of {P} at a rate of {R}% for {T} years is {I}."

Call print_interest with sample values (e.g., principal=1000, rate=5, time=3).
'''

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def print_interest(principal, rate, time):
    interest = calculate_simple_interest(principal, rate, time)
    print(f"The interest for a principal of {principal} at a rate of {rate}% for {time} years is {interest}.")

# Example call.
print_interest(1000, 5, 3)