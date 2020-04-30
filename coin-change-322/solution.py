from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        sub_prob_arr = [amount + 1] * (amount + 1)

        sub_prob_arr[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    sub_prob_arr[i] = min(
                        sub_prob_arr[i], 1 + sub_prob_arr[i - coin])
                else:
                    break

        if sub_prob_arr[amount] > amount:
            return -1
        else:
            return sub_prob_arr[amount]


s = Solution()
print(s.coinChange([1, 2, 5], 11))
