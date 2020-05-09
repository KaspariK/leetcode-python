from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        # Break down the string into "sub problems", then solve each of
        # those and eventually build up to solving the collective problem

        # Create array of len(s) + 1 to account for 0 length strings
        # This will store the number of ways to decode a string of length n
        sub_problem_arr = [0] * (len(s) + 1)

        # Number of ways to decode a string of length 0
        sub_problem_arr[0] = 1

        # Number of ways to decode a string of length 1
        sub_problem_arr[1] = 0 if s[0] == "0" else 1

        # Starting at 2, we can solve the remainder of the "sub problems"
        for i in range(2, len(s) + 1):
            # Since our code includes up to 26 for a single char we need to grab
            # both the current digit as well as the current digit and the one before
            single_digit = int(s[i-1])
            double_digit = int(s[i-2:i])

            if single_digit >= 1:
                sub_problem_arr[i] += sub_problem_arr[i - 1]

            if double_digit >= 10 and double_digit <= 26:
                sub_problem_arr[i] += sub_problem_arr[i - 2]

        # The array stores the number of ways to decode a string of length n, return index n
        return sub_problem_arr[len(s)]
