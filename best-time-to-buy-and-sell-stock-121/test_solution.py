import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 5)

    def test_solution_negative_case(self):
        s = Solution()

        result = s.maxProfit([7, 6, 5, 4, 3])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
