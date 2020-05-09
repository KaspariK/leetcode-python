class Solution:
    def countSubstrings(self, s: str) -> int:
        trans_s = '|'.join('${}@'.format(s))

        pal_lengths = [0] * len(trans_s)

        center = 1
        right = 1

        for i in range(1, len(trans_s) - 1):
            mirror = 2 * center - i

            if right >= i:
                pal_lengths[i] = min(right - i, pal_lengths[mirror])

            while trans_s[i + (1 + pal_lengths[i])] == trans_s[i - (1 + pal_lengths[i])]:
                pal_lengths[i] += 1

            if i + pal_lengths[i] > right:
                center = i
                right = i + pal_lengths[i]

        return sum((length + 1)//2 for length in pal_lengths)
