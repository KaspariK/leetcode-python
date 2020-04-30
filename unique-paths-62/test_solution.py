import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_uniquePaths(self):
        s = Solution()

        result = s.uniquePaths(7, 3)
        self.assertEqual(result, 28)


if __name__ == "__main__":
    unittest.main()
