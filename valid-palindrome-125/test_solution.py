import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        s = Solution()

        result = s.isPalindrome("Racecar")
        self.assertEqual(result, True)

    def test_isPalindrome_with_non_alphanumeric_chars(self):
        s = Solution()

        result = s.isPalindrome("A man, a plan, a canal: Panama")
        self.assertEqual(result, True)

    def test_isPalindrome_false(self):
        s = Solution()

        result = s.isPalindrome("race a car")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
