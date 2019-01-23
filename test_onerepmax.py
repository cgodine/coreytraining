import unittest
import onerepmax

class TestOneRepMax(unittest.TestCase):

    def test_calculate_one_rep_max(self):
        self.assertEqual(onerepmax.calculate_one_rep_max(500, 1), 500)
        self.assertEqual(onerepmax.calculate_one_rep_max(1000000, 1), 1000000)
        self.assertNotEqual(onerepmax.calculate_one_rep_max(95,3), 95)

if __name__ == '__main__':
    unittest.main()