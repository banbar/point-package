from point import Point
import math

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in a 2D space.

    :param tuple point1: The first point as (x, y).
    :param tuple point2: The second point as (x, y).
    :return: The Euclidean distance between the two points.
    :rtype: float
    """
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

def is_point_inside_polygon(point, polygon):
    """
    Determine whether a point is inside a given polygon using the ray-casting algorithm,
    with additional handling for points on the polygon's boundary.

    :param Point point: The point to check.
    :param list polygon: A list of Point objects representing the polygon vertices.
    :return: True if the point is inside the polygon or on the boundary, False otherwise.
    :rtype: bool
    """
    x, y = point.x, point.y
    n = len(polygon)
    inside = False

    # Check if the point is exactly on a vertex
    if point in polygon:
        return True  # Point is a vertex, so it's inside

    p1 = polygon[0]
    for i in range(n + 1):
        p2 = polygon[i % n]

        # Check if the point is on an edge of the polygon
        if (min(p1.y, p2.y) <= y <= max(p1.y, p2.y)) and (min(p1.x, p2.x) <= x <= max(p1.x, p2.x)):
            cross_product = (x - p1.x) * (p2.y - p1.y) - (y - p1.y) * (p2.x - p1.x)
            if abs(cross_product) < 1e-9:  # If cross-product is 0, the point is on the edge
                return True

        # Ray-casting algorithm (unchanged)
        if min(p1.y, p2.y) < y <= max(p1.y, p2.y) and x <= max(p1.x, p2.x):
            if p1.y != p2.y:
                xinters = (y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x
            if p1.x == p2.x or x <= xinters:
                inside = not inside

        p1 = p2

    return inside


def closest_point(target_point, points):
    """
    Find the closest point to a given target point from a list of points.

    :param Point target_point: The target point.
    :param list points: A list of Point objects.
    :return: The closest point from the list.
    :rtype: Point
    """
    return min(points, key=lambda p: target_point.distance_to(p))
