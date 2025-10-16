'''
Exercise: Leap Year Checker
Write a program that determines if a given year is a leap year using several subfunctions and float numbers. Do not use loops.

Define a function called is_divisible that takes two float numbers and returns True if the first is divisible by the second, otherwise False.
Define a function called divisible_by_4 that takes a float year and returns True if the year is divisible by 4 (use is_divisible).
Define a function called divisible_by_100 that takes a float year and returns True if the year is divisible by 100 (use is_divisible).
Define a function called divisible_by_400 that takes a float year and returns True if the year is divisible by 400 (use is_divisible).
Define a function called is_leap_year that takes a float year and returns True if the year is a leap year, otherwise False.
A year is a leap year if it is divisible by 4, and either not divisible by 100, or divisible by 400.
'''

def is_divisible(a, b):
    return a % b == 0

def divisible_by_4(year):
    return is_divisible(year, 4)

def divisible_by_100(year):
    return is_divisible(year, 100)

def divisible_by_400(year):
    return is_divisible(year, 400)

def is_leap_year(year):
    return (divisible_by_4(year) and not divisible_by_100(year)) or divisible_by_400(year)

# Example calls.
print(is_leap_year(2000)) # True.
print(is_leap_year(1900)) # False.
print(is_leap_year(2024)) # True.
print(is_leap_year(2023)) # False.