import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_maxSubArray(self):
        s = Solution()

        result = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(result, 6)

    def test_maxSubArray_false(self):
        s = Solution()

        result = s.maxSubArray([-1])
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
