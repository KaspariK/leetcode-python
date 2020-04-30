
import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_maxDepth(self):
        s = Solution()

        result = s.maxDepth([3, 9, 20, None, None, 15, 7])
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
