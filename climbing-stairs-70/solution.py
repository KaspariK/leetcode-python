class Solution:
    def climbStairs(self, n: int) -> int:
        sub_prob_arr = [0] * (n + 1)

        sub_prob_arr[0] = 1
        sub_prob_arr[1] = 1

        for i in range(2, n + 1):
            sub_prob_arr[i] = sub_prob_arr[i - 1] + sub_prob_arr[i - 2]

        return sub_prob_arr[n]
