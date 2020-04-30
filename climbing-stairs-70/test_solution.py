import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_climbStairs(self):
        s = Solution()

        result = s.climbStairs(4)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
