import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.findMin([3, 4, 5, 1, 2])
        self.assertEqual(result, 1)

    def test_single_int(self):
        s = Solution()

        result = s.findMin([3])
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
