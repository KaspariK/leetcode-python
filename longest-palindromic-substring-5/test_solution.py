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

    # Same tests done for Manacher's Algorithm

    def test_manachers_single_character_center(self):
        s = Solution()

        result = s.manachersLongestPalindrome("aba")
        self.assertEqual(result, "aba")

    def test_manachers_double_character_center(self):
        s = Solution()

        result = s.manachersLongestPalindrome("abba")
        self.assertEqual(result, "abba")

    def test_manachers_empty_string(self):
        s = Solution()

        result = s.manachersLongestPalindrome("")
        self.assertEqual(result, "")

    def test_manachers_one_char_string(self):
        s = Solution()

        result = s.manachersLongestPalindrome("a")
        self.assertEqual(result, "a")

    def test_manachers_one_char_palindrome(self):
        s = Solution()

        result = s.manachersLongestPalindrome("abc")
        self.assertEqual(result, "a")


if __name__ == "__main__":
    unittest.main()
