import unittest
from solution import Solution


class TestAdd(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
