import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.minWindow("ADOBECODEBANC", "ABC")
        self.assertEqual(result, "BANC")

    def test_string_not_present(self):
        s = Solution()

        result = s.minWindow("KEVINISCOOL", "ABC")
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
