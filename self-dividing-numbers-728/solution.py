class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        selfDividingNums = []

        while (left <= right):
            left_string = str(left)
            result = 0

            for ch in left_string:
                digit = int(ch)

                if digit == 0:
                    result += 1
                    break

                if (left % digit) == 0:
                    result += 0
                else:
                    result += 1

            if result == 0:
                selfDividingNums.append(left)

            left += 1

        return selfDividingNums
