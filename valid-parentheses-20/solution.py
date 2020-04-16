class Solution:
    def isValid(self, s: str) -> bool:
        # Track open parentheses in str using stack
        stack = []
        parenthesis_map = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            # Push open parentheses into stack
            if char in parenthesis_map:
                stack.append(char)
            else:
                # If popped element doesn't pair with current char it is an invalid string
                if not stack or parenthesis_map[stack.pop()] != char:
                    return False
        return not stack


s = Solution()

print(s.isValid("]"))
