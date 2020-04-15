class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)

        if str_length <= 1:
            return s
