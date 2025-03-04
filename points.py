"""
point_analysis.py

This module provides functions for performing point analysis in a 2D environment.
"""
import math

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in a 2D space.

    :param tuple point1: The first point as (x, y).
    :param tuple point2: The second point as (x, y).
    :return: The Euclidean distance between the two points.
    :rtype: float
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def is_point_inside_polygon(point, polygon):
    """
    Determine whether a point is inside a given polygon using the ray-casting algorithm,
    with additional handling for points on the polygon's boundary.

    :param tuple point: The point as (x, y).
    :param list polygon: A list of tuples representing the polygon vertices [(x1, y1), (x2, y2), ...].
    :return: True if the point is inside the polygon or on the boundary, False otherwise.
    :rtype: bool
    """
    x, y = point
    n = len(polygon)
    inside = False

    # Check if the point is exactly on a vertex
    if point in polygon:
        return True  # Point is a vertex, so it's inside

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]

        # Check if the point is on an edge of the polygon
        if (p1y <= y <= p2y or p2y <= y <= p1y) and (p1x <= x <= p2x or p2x <= x <= p1x):
            cross_product = (x - p1x) * (p2y - p1y) - (y - p1y) * (p2x - p1x)
            if abs(cross_product) < 1e-9:  # If cross-product is 0, the point is on the edge
                return True

        # Ray-casting algorithm (unchanged)
        if min(p1y, p2y) < y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            if p1x == p2x or x <= xinters:
                inside = not inside

        p1x, p1y = p2x, p2y

    return inside


def closest_point(target_point, points):
    """
    Find the closest point to a given target point from a list of points.

    :param tuple target_point: The target point as (x, y).
    :param list points: A list of points [(x1, y1), (x2, y2), ...].
    :return: The closest point from the list.
    :rtype: tuple
    """
    return min(points, key=lambda p: euclidean_distance(target_point, p))
