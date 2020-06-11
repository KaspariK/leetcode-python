import unittest
from solution import Solution
from solution import ListNode


class TestSolution(unittest.TestCase):
    def test_mergeTwoLists(self):
        s = Solution()

        l1 = ListNode([1, 2, 4])
        l2 = ListNode([1, 3, 4])

        result = s.mergeTwoLists(l1, l2)
        expected = ListNode([1, 1, 2, 3, 4, 4])

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
