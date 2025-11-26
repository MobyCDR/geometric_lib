import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    
    def test_area_positive_values(self):
        res = area(5, 10)
        self.assertEqual(res, 50)
    
    def test_area_zero_width(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_area_zero_height(self):
        res = area(0, 10)
        self.assertEqual(res, 0)
    
    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_area_float_values(self):
        res = area(2.5, 4.5)
        self.assertAlmostEqual(res, 11.25, places=5)
    
    def test_perimeter_positive_values(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)
    
    def test_perimeter_zero_width(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)
    
    def test_perimeter_zero_height(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)
    
    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_perimeter_float_values(self):
        res = perimeter(3.5, 2.5)
        self.assertAlmostEqual(res, 12.0, places=5)


if __name__ == '__main__':
    unittest.main()
