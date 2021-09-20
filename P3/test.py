from OddSeries2 import OddSeries2 as OddSeries
import unittest

class TestOddSeries(unittest.TestCase):
    def test_with_3(self):
        obj = OddSeries()
        self.assertEqual(obj.generate_odd_series(3), [1, 3, 5])
    def test_with_4(self):
        obj = OddSeries()
        self.assertEqual(obj.generate_odd_series(4), [1, 3, 5])
    def test_with_5(self):
        obj = OddSeries()
        self.assertEqual(obj.generate_odd_series(5), [1, 3, 5, 7, 9])
    def test_with_6(self):
        obj = OddSeries()
        self.assertEqual(obj.generate_odd_series(6), [1, 3, 5, 7, 9])

if __name__=='__main__':
    unittest.main()