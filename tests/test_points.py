import unittest
from preprocess import *
from distance_between_points import haversine_distance, euclidean_distance
from haversine import haversine, Unit

class TestPointAnalysis(unittest.TestCase):
    point_a = (58.3810108,26.7187655)
    point_b = (58.3807102,26.7172642)
    
    def test_haversine_distance(self):
        self.assertLessEqual(haversine_distance(self.point_a[0], self.point_a[1], self.point_b[0], self.point_b[1] ), 0.095)
    
    def test_haversine_package(self):
        self.assertLessEqual(haversine(self.point_a, self.point_b), 0.095)

    def test_euclidean_distance(self):
        p1 = point("A", 0,0, "A")
        p2 = point("B", 3,4, "B")
        self.assertEqual(euclidean_distance(p1,p2), 5)

if __name__ == "__main__":
    unittest.main()


