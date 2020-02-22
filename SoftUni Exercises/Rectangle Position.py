fR = input('First rectangle - x, y(points to start), width, height: ')
sR = input('Second rectangle - x, y(points to start), width, height: ')
fR = [int(x) for x in fR.split()]
sR = [int(x) for x in sR.split()]

inside = False

class Rectangle:

    # Constructor
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.x1 = x + width
        self.y1 = y + height
    
fRect = Rectangle(fR[0], fR[1], fR[2], fR[3])
sRect = Rectangle(sR[0], sR[1], sR[2], sR[3])

# Checking if the first rect is inside the second one
if fRect.x >= sRect.x and fRect.y >= sRect.y: # First Points
    if fRect.x1 <= sRect.x1 and fRect.y1 <= sRect.y1: # Second pair of points
        inside = True

if inside == True:
    print('Inside')
else:
    print('Not inside')
