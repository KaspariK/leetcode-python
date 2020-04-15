from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_nums = []

        while (left <= right):
            left_string = str(left)
            neg_result_counter = 0

            for char in left_string:
                digit = int(char)

                if digit == 0:
                    neg_result_counter += 1
                    break

                if (left % digit) == 0:
                    neg_result_counter += 0
                else:
                    neg_result_counter += 1
                    break

            if neg_result_counter == 0:
                self_dividing_nums.append(left)

            left += 1

        return self_dividing_nums
