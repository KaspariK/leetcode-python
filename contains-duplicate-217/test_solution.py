import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution_true(self):
        s = Solution()

        result = s.containsDuplicate([1, 2, 3, 1])
        self.assertEqual(result, True)

    def test_solution_negative_case(self):
        s = Solution()

        result = s.containsDuplicate([1, 2, 3, 4])
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
