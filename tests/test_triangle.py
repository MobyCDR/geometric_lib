import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    
    def test_area_positive_values(self):
        res = area(10, 5)
        self.assertEqual(res, 25)
    
    def test_area_zero_base(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
    
    def test_area_zero_height(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_area_unit_values(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)
    
    def test_area_float_values(self):
        res = area(5.5, 4.0)
        self.assertAlmostEqual(res, 11.0, places=5)
    
    def test_area_large_values(self):
        res = area(100, 50)
        self.assertEqual(res, 2500)
    
    def test_perimeter_positive_values(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_perimeter_equal_sides(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)
    
    def test_perimeter_zero_side(self):
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)
    
    def test_perimeter_float_values(self):
        res = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(res, 10.0, places=5)
    
    def test_perimeter_unit_values(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)
    
    def test_perimeter_large_values(self):
        res = perimeter(100, 200, 150)
        self.assertEqual(res, 450)


if __name__ == '__main__':
    unittest.main()
