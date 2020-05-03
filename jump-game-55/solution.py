from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_successful_index = len(nums) - 1

        # Starting at the end of the list, determine whether the next index back is able to reach the
        # last_successful_index. If yes, reassign last_successful_index to the current index and proceed
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= last_successful_index:
                last_successful_index = i

        return last_successful_index == 0
