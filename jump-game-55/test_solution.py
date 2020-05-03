import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_canJump(self):
        s = Solution()

        result = s.canJump([2, 3, 1, 1, 4])
        self.assertEqual(result, True)

    def test_canJump_false(self):
        s = Solution()

        result = s.canJump([3, 2, 1, 0, 4])
        self.assertEqual(result, False)

    def test_canJump_else_condition_false(self):
        s = Solution()

        result = s.canJump([2, 0, 0])
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
