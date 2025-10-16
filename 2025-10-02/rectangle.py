'''
Exercise: Rectangle Area and Perimeter Calculator
Define a function called calculate_area.
The function should:
- Take two parameters: length and width (both numbers).
- Calculate the area of the rectangle (length * width).
- Return the area.

Define a function called calculate_perimeter.
The function should:
- Take two parameters: length and width.
- Calculate the perimeter of the rectangle (2 * (length + width)).
- Return the perimeter.

Define a function called print_rectangle_info.
The function should:
- Take length and width as parameters.
- Call calculate_area and calculate_perimeter.
- Print the messages:
  "Area: {area}"
  "Perimeter: {perimeter}"

Call print_rectangle_info with sample values (e.g., length=5, width=3).
'''

def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def print_rectangle_info(length, width):
    a = calculate_area(length, width)
    p = calculate_perimeter(length, width)
    print(f"Area: {a}")
    print(f"Perimeter: {p}")

# Example call.
print_rectangle_info(5, 3)