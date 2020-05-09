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

    # I've spent basically the last 3-4 days reading about Manacher's algorithm so
    # I'd like to give it a go here. If it works, time complexity will go from
    # quadratic or O(n^2) to linear or O(n)

    # In all my research, this https://tarokuriyama.com/projects/palindrome2.php#linear_algo
    # has been the most helpful explanation. Truly, a fantastic resource.

    # The key to saving effort expended in the quadratic algorithm is to remove the
    # repeated work, and we can take advantage of certain palindromic properties to do so.
    #
    # The property in question is that palindromes are reflections of themselves around a center
    # character. Let's use the string "ababa" while considering this property. The longest
    # sub-string palindrome here is the entire string itself. In the initial solution we would
    # iterate over each character, treating it as our palindrome center, and expand to the left
    # and right until the character on the left and the character on the right we no longer equivalent.
    #
    # In the case of "ababa" the palindrome using the first "b" as its center is equivalent to the
    # palindrome using the second "b" as its center, but we were still checking them as if we didn't have
    # this information. Manacher's Algorithm relies on this to give us a jump start of sorts when expanding
    # around a center.
    #
    # By the time we get to the second "b" we've already expanded around the second "a" and found a
    # palindrome of length 5. This palindrome iteself contains the two "b's" and they are compliments of
    # one another in that they are the same distance from the center character. This information lets us
    # know that the second "b" is at least as large as the palindrome we found centered on the first "b."
    #
    # Using this info we start our expansion to the left and right further than we would without knowing
    # this info. In this case the palindrome around the first "b" is of length 3, so we know that the second
    # "b" is at least that large. We can start expanding from a palindrome of length 3.
    #
    # I hope that made some sense. If it doesn't, I get it. I've been wracking my brain over this for a while
    # and I can promise that once you get it, it will seem so simple that you'll wonder how you never
    # saw it in the first place.

    def manachersLongestPalindrome(self, s: str) -> str:
        # Transform the incoming string by inserting special character between each character in the string
        # This ensures that we are always dealing with odd length palindromes and can expand around a single
        # center point. $ and @ just help indicate that we are at the string's edge.
        #
        # Ex. The string "ababa" becomes "$|a|b|a|b|a|@"
        trans_s = '|'.join('${}@'.format(s))

        # As we expand around each character we will store each characters palindrome length in a list of
        # length len(s). We also count the palindrome length around the special characters ("|")
        #
        #         String =>  $  |  a  |  b  |  a  |  b  |  a  |  @
        #    pal_lengths => [0, 0, 1, 0, 3, 0, 5, 0, 3, 0, 1, 0, 0]
        #
        # We can see that the second "a" is the center of a palindrome of length 5
        pal_lengths = [0] * len(trans_s)

        # Pointers for the palindrome's center and rightmost character
        center = 1
        right = 1

        for i in range(1, len(trans_s) - 1):
            # Mirror is the complementary letter (think of it as a characters reflection on the other side of center)
            mirror = 2 * center - i

            # If the current longest palindrome's rightmost character is beyond i, then we can use the reflection
            # property of that palindrome to get a jumpstart on expanding (as explained above, hopefully)
            if right >= i:
                pal_lengths[i] = min(right - i, pal_lengths[mirror])

            # Expand around center character comparing left and right characters
            while trans_s[i + (1 + pal_lengths[i])] == trans_s[i - (1 + pal_lengths[i])]:
                # If left character == right character, increase the length of the palindrome
                pal_lengths[i] += 1

                # Check if this is now the longest palindrome, if yes, reassign center and right
                if i + pal_lengths[i] > right:
                    center = i
                    right = i + pal_lengths[i]

        max_pal_len = 0
        pal_index = 0

        # Find longest palindrome length in pal_lengths, and the index of the character centering that palindrome
        for i, n in enumerate(pal_lengths):
            if max_pal_len < n:
                pal_index = i
            max_pal_len = max(max_pal_len, n)

        # Create longest palindromic substring using the index and max length of the palindrome
        return s[(pal_index - max_pal_len)//2: (pal_index + max_pal_len)//2]
