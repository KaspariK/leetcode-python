import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = sys.maxsize

        for num in prices:
            min_val = min(min_val, num)
            max_profit = max(max_profit, num - min_val)

        return max_profit
