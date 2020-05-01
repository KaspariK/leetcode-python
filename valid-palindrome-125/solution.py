class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_edge = 0
        right_edge = len(s) - 1

        while left_edge < right_edge:
            if not s[left_edge].isalnum():
                left_edge += 1
            elif not s[right_edge].isalnum():
                right_edge -= 1
            else:
                if s[left_edge].lower() == s[right_edge].lower():
                    left_edge += 1
                    right_edge -= 1
                else:
                    return False

        return True
