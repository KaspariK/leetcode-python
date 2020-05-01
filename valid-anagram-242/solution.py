class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_dict = {}

        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        for char in t:
            if char not in char_dict:
                return False

            if char_dict[char] == 1:
                del char_dict[char]
            else:
                char_dict[char] -= 1

        return len(char_dict) == 0
