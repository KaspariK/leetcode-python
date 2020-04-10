from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        selfDividingNums = []

        while (left <= right):
            leftString = str(left)
            negResultCounter = 0

            for char in leftString:
                digit = int(char)

                if digit == 0:
                    negResultCounter += 1
                    break

                if (left % digit) == 0:
                    negResultCounter += 0
                else:
                    negResultCounter += 1
                    break

            if negResultCounter == 0:
                selfDividingNums.append(left)

            left += 1

        return selfDividingNums
