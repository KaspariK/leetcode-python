import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_maxArea(self):
        s = Solution()

        result = s.containsDuplicate([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(result, 49)


if __name__ == "__main__":
    unittest.main()
