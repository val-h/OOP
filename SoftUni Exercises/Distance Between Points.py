import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def Distance(f, s):
    a = f.x - s.x
    b = f.y - s.y
    c = pow(a, 2) + pow(b, 2)
    return math.sqrt(c)

fPoints = input('x1, y1 = ')
sPoints = input('x2, y2 = ')
x1, y1 = [int(x) for x in fPoints.split()]
x2, y2 = [int(x) for x in sPoints.split()]

p1 = Point(x1, y1)
p2 = Point(x2, y2)

dist = Distance(p1, p2)

print(f'Distance is {dist:.3f}')
