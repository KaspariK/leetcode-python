import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_invertTree(self):
        s = Solution()

        result = s.invertTree([4, 2, 7, 1, 3, 6, 9])
        self.assertEqual(result, [4, 7, 2, 9, 6, 3, 1])


if __name__ == "__main__":
    unittest.main()
