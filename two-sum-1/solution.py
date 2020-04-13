from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {}
        response = []

        for i, num in enumerate(nums):
            if num in targetDict:
                response = [targetDict.get(num), i]
                break
            else:
                targetDict[target-num] = i

        return response
