class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_edge = 0
        right_edge = 0

        longest_sub = 0

        unique_chars = set()

        while right_edge < len(s):
            if s[right_edge] not in unique_chars:
                unique_chars.add(s[right_edge])
                right_edge += 1
                longest_sub = max(longest_sub, right_edge - left_edge)
            else:
                unique_chars.remove(s[left_edge])
                left_edge += 1

        return longest_sub
