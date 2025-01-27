"""A welcoming test program to start COMP110"""

__author__ = "01234567"

print("Welcome to COMP110!")
print("You are in for a fun adventure into programming!")
print("<3 the COMP110 Team!")
"""This module does xyz"""


def perimeter(length: float, width: float) -> float:
    """Calculate the perimeter of a rectangle."""
    return 2 * length + 2 * width


perimeter(length=10.0, width=8.0)


def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))
