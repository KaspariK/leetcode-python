from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # Gauss's formula for the sum of a series will give us the "expected" sum of a series of n length
        # Subtract the actual sum to find the missing value
        return (n * (n + 1) // 2) - sum(nums)
