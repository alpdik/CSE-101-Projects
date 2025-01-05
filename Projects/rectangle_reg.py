
class Area:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Perimeter:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def perimeter(self):
        return 2 * (self.length + self.breadth)

r1=Area(4,5)
print(r1.area())
r2=Perimeter()
r2.length=4
r2.breadth=5
print(r2.perimeter())
