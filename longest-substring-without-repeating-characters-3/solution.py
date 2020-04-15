class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_edge = 0
        right_edge = 0

        max_substring = 0

        unique_chars = set()

        while right_edge < len(s):
            if s[right_edge] not in unique_chars:
                unique_chars.add(s[right_edge])
                right_edge += 1
                max_substring = max(max_substring, right_edge - left_edge)
            else:
                unique_chars.remove(s[left_edge])
                left_edge += 1
        return max_substring
