import unittest
import Unit


class TestUnit(unittest.TestCase):

    def test_add(self):  # name of the method should be begin with test
        self.assertEqual(Unit.add(10, 5), 15)
        self.assertEqual(Unit.add(-1, 1), 0)
        self.assertEqual(Unit.add(-1, -1), -2)

    def test_subtract(self):  # name of the method should be begin with test
        self.assertEqual(Unit.substract(10, 5), 5)
        self.assertEqual(Unit.substract(-1, 1), -2)
        self.assertEqual(Unit.substract(-1, -1), 0)

    def test_multiply(self):  # name of the method should be begin with test
        self.assertEqual(Unit.multiply(10, 5), 50)
        self.assertEqual(Unit.multiply(-1, 1), -1)
        self.assertEqual(Unit.multiply(-1, -1), 1)

    def test_divide(self):  # name of the method should be begin with test
        self.assertEqual(Unit.divide(10, 5), 2)
        self.assertEqual(Unit.divide(-1, 1), -1)
        self.assertEqual(Unit.divide(-1, -1), 1)

        with self.assertRaises(ValueError):
            Unit.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
