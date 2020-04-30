import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        s = Solution()

        result = s.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])


if __name__ == "__main__":
    unittest.main()
