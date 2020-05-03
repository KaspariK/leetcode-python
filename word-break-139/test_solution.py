import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_wordBreak(self):
        s = Solution()

        result = s.wordBreak("leetcode", ["leet", "code"])
        self.assertEqual(result, True)

    def test_wordBreak_repeated_word(self):
        s = Solution()

        result = s.wordBreak("applepenapple", ["apple", "pen"])
        self.assertEqual(result, True)

    def test_wordBreak_false(self):
        s = Solution()

        result = s.wordBreak(
            "catsandog", ["cats", "dog", "sand", "and", "cat"])
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
