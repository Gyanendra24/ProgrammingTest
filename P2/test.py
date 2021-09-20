from OddSeries import OddSeries
import unittest

class TestOddSeries(unittest.TestCase):
    def test_with_5(self):
        obj = OddSeries()
        self.assertEqual(obj.generate_odd_series(5), [1, 3, 5, 7, 9])
    def test_with_7(self):
        obj = OddSeries()
        self.assertEqual(obj.generate_odd_series(7), [1, 3, 5, 7, 9, 11, 13])

if __name__=='__main__':
    unittest.main()