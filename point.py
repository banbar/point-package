import math

class Point:
    """A class to represent a point in a 2D space."""
    
    def __init__(self, x, y):
        """
        Initialize a point with x and y coordinates.
        
        :param float x: X-coordinate of the point.
        :param float y: Y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def distance_to(self, other):
        """
        Calculate the Euclidean distance to another point.
        
        :param Point other: The other point.
        :return: The Euclidean distance.
        :rtype: float
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __eq__(self, other):
        """Check if two points are equal."""
        return isinstance(other, Point) and math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __repr__(self):
        """String representation of the point."""
        return f"Point({self.x}, {self.y})"
