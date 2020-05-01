import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_groupAnagrams(self):
        s = Solution()

        result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(
            result, [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    def test_groupAnagrams_empty_list(self):
        s = Solution()

        result = s.groupAnagrams([""])
        self.assertEqual(result, [[""]])


if __name__ == "__main__":
    unittest.main()
