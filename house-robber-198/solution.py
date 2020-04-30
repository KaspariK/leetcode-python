from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        # Break primary problem down into sub-problems (ie. whats the max amount I can rob at each index)
        sub_prob_arr = [0] * len(nums)

        # Fill first two spots with default values
        sub_prob_arr[0] = nums[0]
        sub_prob_arr[1] = max(nums[0], nums[1])

        # Start at index 2 since first two spots are filled above
        for i in range(2, len(nums)):
            # The most money we can rob at this position(i) is the greater of the amount we could
            # rob at the previous house's index and the amount we could rob at the second house back
            sub_prob_arr[i] = max(sub_prob_arr[i - 1],
                                  nums[i] + sub_prob_arr[i - 2])

        # Last item of the array contains max robbery amount
        return sub_prob_arr[-1]

# Space complexity can be reduced by not using an entire
# sub-problem array, seeing as we only ever look two values back
