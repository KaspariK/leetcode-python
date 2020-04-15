import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.productExceptSelf([4, 5, 1, 8, 2])
        self.assertEqual(result, [80, 64, 320, 40, 160])


if __name__ == "__main__":
    unittest.main()
