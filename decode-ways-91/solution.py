from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        sub_problem_arr = [0] * (len(s) + 1)

        sub_problem_arr[0] = 1
        sub_problem_arr[1] = 0 if s[0] == "0" else 1

        for i in range(1, len(s) + 1):
            one_digit = int(s[i-1])
            two_digit = int(s[i-2:i])

            if one_digit >= 1:
                sub_problem_arr[i] += sub_problem_arr[i - 1]

            if two_digit >= 10 and two_digit <= 26:
                sub_problem_arr[i] += sub_problem_arr[i - 2]

        return sub_problem_arr[len(s)]
