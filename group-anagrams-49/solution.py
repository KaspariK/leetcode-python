from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}

        for string in strs:
            # Sorting was the clear path here but the tuple key was new to me. Since it's immutable it can
            # be used as a key, the alternative being a weird string join which I think looks stupid and messy
            key = tuple(sorted(string))

            # Key is sorted string as tuple
            # Value is unsorted string
            if key in str_dict:
                str_dict[key].append(string)
            else:
                str_dict[key] = [string]

        return str_dict.values()


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
