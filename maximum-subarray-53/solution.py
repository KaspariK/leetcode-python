from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = nums[0]
        cur_max = 0

        for num in nums:
            cur_max += num

            max_sum = max(max_sum, cur_max)

            if cur_max <= 0:
                cur_max = 0

        return max_sum
