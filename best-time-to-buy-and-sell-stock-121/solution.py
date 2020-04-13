import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = sys.maxsize

        for num in prices:
            if num < minVal:
                minVal = num
            else:
                maxProfit = max(maxProfit, num - minVal)

        return maxProfit
