import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        s = Solution()

        result = s.lengthOfLongestSubstring("aaa")
        self.assertEqual(result, 1)

    def test_lengthOfLongestSubstring_length_greater_than_1(self):
        s = Solution()

        result = s.lengthOfLongestSubstring("abcdeekrcsty")
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
