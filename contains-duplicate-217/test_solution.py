import unittest
from solution import Solution


class TestAdd(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        result = s.containsDuplicate([1, 2, 3, 1])
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
