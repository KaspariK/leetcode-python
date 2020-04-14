import unittest
from solution import Solution


class TestAdd(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.longestPalindrome("aaa")
        self.assertEqual(result, 3)

    def test_solution_length_greater_than_1(self):
        s = Solution()

        result = s.longestPalindrome("abcbadefthyu")
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
