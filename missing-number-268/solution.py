from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # Gauss's formula for the sum of a series will give us the "expected" sum of a series of n length
        # Subtract the actual sum to find the missing value
        return (n * (n + 1) // 2) - sum(nums)

    def missingNumberXOR(self, nums: List[int]) -> int:
        # XOR has some properties that are really helpful in solving this
        #
        # Commutative: a ^ b = b ^ a so input order doesn't matter
        # Associative: a ^ (b ^ c) = (a ^ b) ^ c so operations can be chained in anyorder
        # Self inverse: a ^ a = 0 so any value XOR'd with itself returns zero
        #
        # Also, XOR helps avoid any potential overflow concerns (not a huge concern with Python, but still) as a result of summation

        total_xor = 0
        list_xor = 0

        # XOR of all values in complete series
        for i in range(1, len(nums) + 1):
            total_xor ^= i

        # XOR of all values in incomplete series
        for num in nums:
            list_xor ^= num

        return total_xor ^ list_xor
