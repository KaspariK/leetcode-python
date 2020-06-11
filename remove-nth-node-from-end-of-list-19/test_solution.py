import unittest
from solution import Solution
from solution import ListNode


class TestSolution(unittest.TestCase):
    def test_removeNthFromEnd(self):
        s = Solution()

        l1 = ListNode([1, 2, 3, 4, 5])

        result = s.removeNthFromEnd(l1, 2)
        expected = ListNode([1, 2, 3, 5])

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
