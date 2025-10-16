'''
Exercise: Temperature Converter (Function Parameter Version)
Define a function called celsius_to_fahrenheit.
The function should:
- Take a temperature in Celsius as a parameter.
- Convert it to Fahrenheit using the formula: F = C * 9/5 + 32.
- Return the Fahrenheit temperature.

Define a function called print_conversion.
The function should:
- Take a Celsius temperature as a parameter.
- Call celsius_to_fahrenheit to get the Fahrenheit value.
- Print the message: "The temperature {C}°C is {F}°F."

Call print_conversion with a sample Celsius temperature (e.g., 25).
'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def print_conversion(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"The temperature {celsius}°C is {fahrenheit}°F")

# Example call.
print_conversion(25)