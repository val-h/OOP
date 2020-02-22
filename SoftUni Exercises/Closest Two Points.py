import sys
import math
n = int(input('Times to repeat: '))
points = {}
diff = sys.maxsize

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def Distance(p1, p2):
    a = abs(p1.x - p2.x)
    b = abs(p1.y - p2.y)
    c = pow(a, 2) + pow(b, 2)
    return math.sqrt(c)


for i in range(0, n):
    usrInp = input('x and y - ')
    x, y = [int(x) for x in usrInp.split()]
    points[i] = x, y

# TODO > finish the distance logic
