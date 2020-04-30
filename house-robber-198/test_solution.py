import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_rob(self):
        s = Solution()

        result = s.rob([1, 2, 3, 1])
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
