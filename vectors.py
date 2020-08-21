"""Class interactions explained by NeuralNine."""

class Vector:
    """Class to represent a vector."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define what happens when you add this class to another object
    # in this case - another vector
    def __add__(self, other):
        """Defines the functionality of adding 2 vectors."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Defines the functionality of subtracting 2 vectors."""
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        """String representation of the vector."""
        return f'X: {self.x}\nY: {self.y}'
    
v1 = Vector(5, 3)
v2 = Vector(7, 4)

print(v1)
print(v2)

v3 = v1 + v2
v4 = v3 - v1

print(v3)
print(v4)
