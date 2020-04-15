from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)

        left_products = [None] * nums_length
        right_products = [None] * nums_length

        left_products[0] = 1
        right_products[nums_length - 1] = 1

        for i in range(1, nums_length, 1):
            left_products[i] = left_products[i-1] * nums[i-1]

        for i in range(nums_length - 2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]

        output_products = [None] * nums_length

        for i in range(nums_length):
            output_products[i] = left_products[i] * right_products[i]

        return output_products
