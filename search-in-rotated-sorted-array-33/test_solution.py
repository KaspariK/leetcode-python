import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_search(self):
        s = Solution()

        result = s.search([4, 5, 6, 7, 0, 1, 2], 0)
        self.assertEqual(result, 4)

    def test_search_false(self):
        s = Solution()

        result = s.search([4, 5, 6, 7, 0, 1, 2], 3)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
