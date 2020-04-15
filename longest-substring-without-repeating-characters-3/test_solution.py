import unittest
from solution import Solution


class TestAdd(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.lengthOfLongestSubstring("aaa")
        self.assertEqual(result, 1)

    def test_solution_length_greater_than_1(self):
        s = Solution()

        result = s.lengthOfLongestSubstring("abcdeekrcsty")
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()