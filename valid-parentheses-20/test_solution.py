import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_empty(self):
        s = Solution()

        result = s.isValid("")
        self.assertEqual(result, True)

    def test_isValid_simple(self):
        s = Solution()

        result = s.isValid("()")
        self.assertEqual(result, True)

    def test_isValid_complex(self):
        s = Solution()

        result = s.isValid("([[()()]{()}]{})")
        self.assertEqual(result, True)

    def test_isValid_simple_false(self):
        s = Solution()

        result = s.isValid("]")
        self.assertEqual(result, False)

    def test_isValid_complex_false(self):
        s = Solution()

        result = s.isValid("{([)][()]}")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
