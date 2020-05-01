import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_isSameTree(self):
        s = Solution()

        result = s.isSameTree([1, 2, 3], [1, 2, 3])
        self.assertEqual(result, True)

    def test_isSameTree_false(self):
        s = Solution()

        result = s.isSameTree([1, 2], [1, None, 2])
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
