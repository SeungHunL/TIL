class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Rectangle(Point):
    def __init__(self, o1, o2):
        self.x = o2.x - o1.x
        self.y = o1.y - o2.y
    def get_area(self):
        return self.x * self.y
    def get_perimeter(self):
        return 2*(self.x + self.y)
    def is_square(self):
        if self.x == self.y:
            return True
        else:
            return False     
p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3,p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
