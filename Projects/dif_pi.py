class Circle:
    def __init__(self, radius, pi=3):
        self.radius = radius
        self.pi = pi

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius

c1=Circle(4,3.14)
print(c1.area())
print(c1.circumference())
c2=Circle(4)
print(c2.area())
print(c2.circumference())