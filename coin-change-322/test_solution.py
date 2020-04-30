import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_coinChange_simple(self):
        s = Solution()

        result = s.coinChange([1, 2, 5], 11)
        self.assertEqual(result, 3)

    def test_coinChange_complex(self):
        s = Solution()

        result = s.coinChange([25, 10, 1], 31)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
