import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    
    def test_area_positive_radius(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25, places=5)
    
    def test_area_zero_radius(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area_unit_radius(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi, places=5)
    
    def test_area_float_radius(self):
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 6.25, places=5)
    
    def test_perimeter_positive_radius(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5, places=5)
    
    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_unit_radius(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi, places=5)
    
    def test_perimeter_float_radius(self):
        res = perimeter(3.7)
        self.assertAlmostEqual(res, 2 * math.pi * 3.7, places=5)


if __name__ == '__main__':
    unittest.main()
