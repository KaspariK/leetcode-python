import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_single_character_center(self):
        s = Solution()

        result = s.longestPalindrome("aba")
        self.assertEqual(result, "aba")

    def test_longestPalindrome_double_character_center(self):
        s = Solution()

        result = s.longestPalindrome("abba")
        self.assertEqual(result, "abba")

    def test_longestPalindrome_empty_string(self):
        s = Solution()

        result = s.longestPalindrome("")
        self.assertEqual(result, "")

    def test_longestPalindrome_one_char_string(self):
        s = Solution()

        result = s.longestPalindrome("a")
        self.assertEqual(result, "a")

    def test_longestPalindrome_one_char_palindrome(self):
        s = Solution()

        result = s.longestPalindrome("abc")
        self.assertEqual(result, "a")


if __name__ == "__main__":
    unittest.main()
