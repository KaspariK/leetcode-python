import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_selfDividingNumbers(self):
        s = Solution()

        result = s.selfDividingNumbers(1, 22)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

    def test_selfDividingNumbers_false(self):
        s = Solution()

        result = s.selfDividingNumbers(13, 14)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
