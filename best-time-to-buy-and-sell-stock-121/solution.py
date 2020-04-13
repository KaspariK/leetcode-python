from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = prices[0]

        for num in prices:
            if num < minVal:
                minVal = num
            else:
                maxProfit = max(maxProfit, num - minVal)

        return maxProfit
