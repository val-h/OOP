import sys
import math

# The number of Points
n = int(input('Amount of points: '))

points = {}
diff = sys.maxsize
fLowestPoint = None
sLowestPoint = None

# Class to create the points(objects)
class Point:

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Calculkating distance between two points
def Distance(p1, p2):
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    c = pow(a, 2) + pow(b, 2)
    return math.sqrt(c)

# Assigning the values
for i in range(0, n):
    usrInp = input('x and y: ')
    x, y = [int(x) for x in usrInp.split()]
    points[i] = x, y

# Looping through every point and checking the distance
for i in range(0, len(points)): # Starting from the first point
    for j in range(i + 1, len(points)): # Starting from the next point and going through the rest
        if Distance(points[j], points[i]) < diff: # Checking the distance between points
            diff = Distance(points[j], points[i]) # Assigning the new lowest diff
            fLowestPoint = points[i]
            sLowestPoint = points[j]

# Output
print(f'Smallest difference from from all of the points: {diff:.3f}')
print(f'Point 1: {fLowestPoint}')
print(f'Point 2: {sLowestPoint}')

# Finally the need for comments is demanded
