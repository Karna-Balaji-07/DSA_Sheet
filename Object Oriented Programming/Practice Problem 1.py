'''
Define a circle class to create a circle with radius r using the constructor
define an area() method of the class which calculates the area of the circle
define a perimeter() method of the class which allows you to calculate the perimeter
of the circle
'''

class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        areas = 3.14 * self.r * self.r
        return areas

    def perimeter(self):
        peri = 2 * 3.14 * self.r
        return peri

c1 = Circle(5)
print(c1.area())
print(c1.perimeter())

print("-------")
c1.r = 4
print(c1.area())
print(c1.perimeter())
print("------")
c2 = Circle(4)
print(c2.perimeter())
print(c2.area())