import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution_simple_valid(self):
        s = Solution()

        result = s.isValid("")
        self.assertEqual(result, True)

    def test_solution_simple_valid(self):
        s = Solution()

        result = s.isValid("()")
        self.assertEqual(result, True)

    def test_solution_complex_valid(self):
        s = Solution()

        result = s.isValid("([[()()]{()}]{})")
        self.assertEqual(result, True)

    def test_solution_simple_invalid(self):
        s = Solution()

        result = s.isValid("]")
        self.assertEqual(result, False)

    def test_solution_complex_ivalid(self):
        s = Solution()

        result = s.isValid("{([)][()]}")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
