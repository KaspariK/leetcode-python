import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.threeSum([-1, 0, 1, 2, -1, -4])
        self.assertEqual(result, [[-1, 0, 1], [-1, -1, 2]])

    def test_duplicates(self):
        s = Solution()

        result = s.threeSum([-2, 0, 0, 2, 2])
        self.assertEqual(result, [[-2, 0, 2]])


if __name__ == "__main__":
    unittest.main()
