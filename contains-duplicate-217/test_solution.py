import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_containsDuplicate(self):
        s = Solution()

        result = s.containsDuplicate([1, 2, 3, 1])
        self.assertEqual(result, True)

    def test_containsDuplicate_false(self):
        s = Solution()

        result = s.containsDuplicate([1, 2, 3, 4])
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
