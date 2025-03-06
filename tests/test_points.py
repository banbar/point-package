import unittest
from geometry_utils import euclidean_distance, is_point_inside_polygon, closest_point

class TestPointAnalysis(unittest.TestCase):
    
    def test_euclidean_distance(self):
        self.assertAlmostEqual(euclidean_distance((0, 0), (3, 4)), 5.0)
        self.assertEqual(euclidean_distance((1, 1), (1, 1)), 0.0)
        self.assertAlmostEqual(euclidean_distance((1, 2), (1, 2)), 0.0)
    
    def test_is_point_inside_polygon(self):
        square = [(0, 0), (0, 10), (10, 10), (10, 0)]
        self.assertTrue(is_point_inside_polygon((5, 5), square))  # Inside
        self.assertFalse(is_point_inside_polygon((15, 5), square))  # Outside
        self.assertTrue(is_point_inside_polygon((0, 0), square))  # On vertex
        self.assertTrue(is_point_inside_polygon((10, 5), square))  # On edge
    
    def test_closest_point(self):
        points = [(1, 1), (2, 2), (3, 3)]
        self.assertEqual(closest_point((0, 0), points), (1, 1))
        self.assertEqual(closest_point((2.5, 2.5), points), (2, 2))
        self.assertEqual(closest_point((5, 5), points), (3, 3))

if __name__ == "__main__":
    unittest.main()


