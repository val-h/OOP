from math import sqrt
class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def Intersect(self, c2):
        a = abs(self.x - c2.x)
        b = abs(self.y - c2.y)
        c = a*a + b*b
        d = sqrt(c)
        if d < self.r + c2.r:
            return True
        return False

# User input conversion to list of ints
firstCircle = input('First Circle: ')
secondCircle = input('Second Circle: ')
firstCircle = [int(x) for x in firstCircle.split()]
secondCircle = [int(x) for x in secondCircle.split()]

# Declaring the variables as Circle class instances
firstCircle = Circle(firstCircle[0], firstCircle[1], firstCircle[2])
secondCircle = Circle(secondCircle[0], secondCircle[1], secondCircle[2])

if firstCircle.Intersect(secondCircle) == True:
    print('Yes')
else:
    print('No')
