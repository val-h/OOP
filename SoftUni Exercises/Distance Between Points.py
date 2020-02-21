import math
fPoints = input('x1, y1 = ')
sPoints = input('x2, y2 = ')
x1, y1 = [int(x) for x in fPoints.split()]
x2, y2 = [int(x) for x in sPoints.split()]

a = abs(x1 - x2)
b = abs(y1 - y2)


class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def Distance(self):
        c = math.pow(a, 2) + math.pow(b, 2)
        return math.sqrt(c)

result = Point.