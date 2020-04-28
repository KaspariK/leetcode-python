from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1

        # Basic binary search for lowest value. Search to the left or right of
        # the midpoint depending on its value compared to the last int in the list
        while left_ptr < right_ptr:
            midpoint = left_ptr + right_ptr >> 1

            if nums[midpoint] > nums[right_ptr]:
                left_ptr = midpoint + 1
            else:
                right_ptr = midpoint

        return nums[left_ptr]
