import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_isAnagram(self):
        s = Solution()

        result = s.isAnagram("anagram", "nagaram")
        self.assertEqual(result, True)

    def test_isAnagram_false(self):
        s = Solution()

        result = s.isAnagram("a", "b")
        self.assertEqual(result, False)

    def test_isAnagram_false_diff_length(self):
        s = Solution()

        result = s.isAnagram("anagram", "naram")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
