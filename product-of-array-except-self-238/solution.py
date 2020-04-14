from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)

        leftProducts = [None] * numsLength
        rightProducts = [None] * numsLength

        leftProducts[0] = 1
        rightProducts[numsLength - 1] = 1

        for i in range(1, numsLength, 1):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]

        for i in range(numsLength - 2, -1, -1):
            rightProducts[i] = rightProducts[i+1] * nums[i+1]

        outputProducts = [None] * numsLength

        for i in range(numsLength):
            outputProducts[i] = leftProducts[i] * rightProducts[i]

        return outputProducts
