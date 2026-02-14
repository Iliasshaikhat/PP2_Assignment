import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius * self.radius

r = int(input())
c = Circle(r)

area = c.area()
print(f"{area:.2f}")
