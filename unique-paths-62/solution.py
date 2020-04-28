class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Init sub-problem matrix
        sub_prob_mt = [[0 for x in range(m)] for y in range(n)]

        # Each square in the first row can be reached in 1 valid way
        for i in range(len(sub_prob_mt)):
            sub_prob_mt[i][0] = 1

        # Each square in the first column can be reached in 1 valid way
        for i in range(len(sub_prob_mt[0])):
            sub_prob_mt[0][i] = 1

        for i in range(1, len(sub_prob_mt)):
            for j in range(1, len(sub_prob_mt[0])):
                # The number of ways to reach any other square on the grib is the sum of the
                # ways to reach the square above it and the ways to reach the square below it
                sub_prob_mt[i][j] = sub_prob_mt[i - 1][j] + \
                    sub_prob_mt[i][j - 1]

        return sub_prob_mt[-1][-1]
