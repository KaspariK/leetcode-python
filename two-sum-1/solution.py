from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        response = []

        for i, num in enumerate(nums):
            if num in target_dict:
                response = [target_dict.get(num), i]
                break
            else:
                target_dict[target-num] = i

        return response
