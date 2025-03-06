from point import Point
from geometry_utils import euclidean_distance, is_point_inside_polygon, closest_point

if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    polygon = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]

    print(f"Distance between {p1} and {p2}: {euclidean_distance(p1, p2)}")
    print(f"Is {p1} inside polygon? {is_point_inside_polygon(p1, polygon)}")
    print(f"Closest point to {p2} in polygon: {closest_point(p2, polygon)}")
