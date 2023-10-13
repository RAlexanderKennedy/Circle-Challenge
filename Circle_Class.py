import math

class Circle:

    def __init__(self, radius:float):
        self.radius = radius

    def calculate_diameter(self):
        self.diameter = (self.radius*2)
        return f"Diameter: {self.diameter}"
    def calculate_circumference(self):
        self.circumference = (self.radius*2)*math.pi
        return f"Circumference: {self.circumference}"
    def calculate_area(self):
        self.area = math.pi * (self.radius**2)
        return f"Area: {self.area}"
    def grow(self):
        self.radius = self.radius*2
        return f"New Radius: {self.radius}"

    def get_radius(self):
        return f"Radius{self.radius}"