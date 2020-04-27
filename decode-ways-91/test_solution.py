import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.numDecodings("12")
        self.assertEqual(result, 2)

    def test_solution_longer(self):
        s = Solution()

        result = s.numDecodings("226")
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
