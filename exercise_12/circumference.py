import math

# Define a class named Circle
class Circle:
    def __init__ (self, radius):
        self.radius = radius

    # Define a method named area
    def area(self):
        return math.pi * (self.radius ** 2) 
    
    # Define a method named perimeter
    def perimeter(self):
        return 2 * math.pi * self.radius

# Create an instance of the circle class
circle_radius = Circle(5.7)
print(f"The circle area is {circle_radius.area():.2f} "
      f"and perimeter {circle_radius.perimeter():.2f}")
