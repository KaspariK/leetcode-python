from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftEdge = 0
        rightEdge = 0

        maxSubstring = 0

        uniqueChars = set()

        while rightEdge < len(s):
            if s[rightEdge] not in uniqueChars:
                uniqueChars.add(s[rightEdge])
                rightEdge += 1
                maxSubstring = max(maxSubstring, rightEdge - leftEdge)
            else:
                uniqueChars.remove(s[leftEdge])
                leftEdge += 1
        return maxSubstring
