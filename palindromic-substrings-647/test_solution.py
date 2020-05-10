import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_countSubstrings_single_char_palindromes(self):
        s = Solution()

        result = s.countSubstrings("abc")
        self.assertEqual(result, 3)

    def test_countSubstrings_multi_char_palindromes(self):
        s = Solution()

        result = s.countSubstrings("aaa")
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
