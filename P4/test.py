from Mapping import Mapping
import unittest

class TestMapping(unittest.TestCase):
    def test_count1(self):
        input = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
        exceptedMap = {1:11, 2:8, 3:4, 4:4, 5:3, 6:2, 7:0, 8:1, 9:1}
        obj = Mapping()
        output = obj.operate(input)
        self.assertEquals(output, exceptedMap)

if __name__ == '__main__':
    unittest.main()