class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Compare n to n-1. n-1 will be identical to the left of the least significant digit.
        # n AND n-1 with flip that least significant digit and all digits to the right.
        # Increment the count each time this happens until n is 0
        while n != 0:
            n &= n - 1
            count += 1

        return count
