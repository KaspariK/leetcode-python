import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_missingNumber(self):
        s = Solution()

        actual = s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])

        self.assertEqual(actual, 8)

    def test_missingNumber_short(self):
        s = Solution()

        actual = s.missingNumber([3, 0, 1])

        self.assertEqual(actual, 2)

    def test_missingNumberXOR(self):
        s = Solution()

        actual = s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])

        self.assertEqual(actual, 8)

    def test_missingNumberXOR_short(self):
        s = Solution()

        actual = s.missingNumber([3, 0, 1])

        self.assertEqual(actual, 2)


if __name__ == "__main__":
    unittest.main()
