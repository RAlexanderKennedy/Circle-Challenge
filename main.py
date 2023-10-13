import Circle_Class
import math

print("Welcome to the Circle Tester")
while True:

    input_radius = float(input("Enter a radius:"))

    try:
        this_circle = Circle_Class.Circle(input_radius)
    except ValueError:
        print("please enter a new value")

    print(this_circle.calculate_diameter())
    print(this_circle.calculate_circumference())
    print(this_circle.calculate_area())

    grow = input("Would you like your circle to grow? (y/n)")

    if grow.upper() == "Y":
        print(this_circle.grow())
        print(this_circle.calculate_diameter())
        print(this_circle.calculate_circumference())
        print(this_circle.calculate_area())

    print("Goodbye")

    break