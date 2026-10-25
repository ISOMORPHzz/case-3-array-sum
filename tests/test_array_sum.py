import unittest
from array_sum import sum_negative_between_min_max


class TestArraySum(unittest.TestCase):
    
    def test_basic_case(self):
        arr = [3, -2, 7, -5, 1, -8, 4, -1, 6]
        self.assertEqual(sum_negative_between_min_max(arr), -5)
    
    def test_min_before_max(self):
        arr = [-10, -3, -4, 5, -2]
        # min=-10 (idx 0), max=5 (idx 3)
        # между ними: -3, -4  →  сумма = -7
        self.assertEqual(sum_negative_between_min_max(arr), -7)
    
    def test_no_negative_between(self):
        arr = [1, 5, 2, 3]
        self.assertEqual(sum_negative_between_min_max(arr), 0)
    
    def test_adjacent_min_max(self):
        arr = [5, -1, 3]
        # max=5 (idx 0), min=-1 (idx 1) — между ними элементов нет
        self.assertEqual(sum_negative_between_min_max(arr), 0)
    
    def test_all_negative(self):
        arr = [-1, -5, -3, -2, -4]
        # max=-1 (idx 0), min=-5 (idx 1)
        # между ними элементов нет
        self.assertEqual(sum_negative_between_min_max(arr), 0)
    
    def test_empty_array_raises(self):
        with self.assertRaises(ValueError):
            sum_negative_between_min_max([])


if __name__ == "__main__":
    unittest.main()