from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # I didn't immediately recognize the problem as a dynamic programming one, but
        # we can easily break it down into sub-problems.

        # Convert list into a set because it is a far more efficient structure to search
        word_set = set(wordDict)

        # Include one extra index for the case of an empty string
        sub_prob_arr = [False] * (len(s) + 1)

        sub_prob_arr[0] = True

        # Loop through s finding substrings, each time the substring is in word_set assign a True value in sub_prob_arr at the index of that substrings last char.
        # For instance, sub_prob_arr for string "leetcode" would be [True, False, False, False, True, False, False, False, True]. You can see that
        # the index of the True values line up with the last char of the words in word_set ("t" and "e")
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if sub_prob_arr[i] == True and s[i:j] in word_set:
                    sub_prob_arr[j] = True

        return sub_prob_arr[-1]
