import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    
    def test_area_positive_side(self):
        res = area(5)
        self.assertEqual(res, 25)
    
    def test_area_zero_side(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area_unit_side(self):
        res = area(1)
        self.assertEqual(res, 1)
    
    def test_area_float_side(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25, places=5)
    
    def test_area_large_value(self):
        res = area(100)
        self.assertEqual(res, 10000)
    
    def test_perimeter_positive_side(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    
    def test_perimeter_zero_side(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_unit_side(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
    
    def test_perimeter_float_side(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 14.0, places=5)
    
    def test_perimeter_large_value(self):
        res = perimeter(100)
        self.assertEqual(res, 400)


if __name__ == '__main__':
    unittest.main()
