class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_palindrome = ""

        # Loop through all characters and call expandFromCenter for each single and adjacent pair
        for i in range(len(s)):
            # Odd number palindromes
            odd_palindrome = self.expandFromCenter(i, i, s)

            # Even number palindromes
            even_palindrome = self.expandFromCenter(i, i + 1, s)

            # Keep max existing palindrome
            max_palindrome = max(max_palindrome, odd_palindrome,
                                 even_palindrome, key=len)

        return max_palindrome

    def expandFromCenter(self, left_edge, right_edge, string) -> str:
        palindrome = ""

        # Expand window as long as there is room within the bounds of the string and edge chars are equivalent
        while left_edge >= 0 and right_edge < len(string) and string[left_edge] == string[right_edge]:
            # Save longest palindrome
            palindrome = string[left_edge:right_edge+1]

            left_edge -= 1
            right_edge += 1

        return palindrome
