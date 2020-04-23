from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1

        left_ptr = 0
        right_ptr = len(nums) - 1

        # This will filter down until it lands on the start of the rotated array
        while left_ptr < right_ptr:
            midpoint = left_ptr + right_ptr >> 1

            if nums[midpoint] > nums[right_ptr]:
                left_ptr = midpoint + 1
            else:
                right_ptr = midpoint

        # The lowest value of our rotated array
        rot_start = left_ptr
        left_ptr = 0
        right_ptr = len(nums) - 1

        # Break the array into two "halves" based on the value of target
        #  and identify which half we will search in
        if target >= nums[rot_start] and target <= nums[right_ptr]:
            left_ptr = rot_start
        else:
            right_ptr = rot_start

        # Now that we have the starting point of the array we can run binary search for our target
        while left_ptr <= right_ptr:
            midpoint = left_ptr + right_ptr >> 1

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left_ptr = midpoint + 1
            else:
                right_ptr = midpoint - 1

        return -1
