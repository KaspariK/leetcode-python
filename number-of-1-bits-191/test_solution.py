import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_hammingWeight_3(self):
        s = Solution()

        result = s.hammingWeight(11)
        self.assertEqual(result, 3)

    def test_hammingWeight_1(self):
        s = Solution()

        result = s.hammingWeight(128)
        self.assertEqual(result, 1)

    def test_hammingWeight_31(self):
        s = Solution()

        result = s.hammingWeight(4294967293)
        self.assertEqual(result, 31)


if __name__ == "__main__":
    unittest.main()
