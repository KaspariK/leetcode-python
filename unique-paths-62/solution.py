class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Seems like a good fit for dynamic programming. The number of moves to
        # the end square can be solved by breaking the overall problem (start -> end) into sub-problems
        #
        # Sub-problems in this case would be the move from start -> each cell and create a matrix

        # Init sub-problem matrix
        sub_prob_mt = [[0 for x in range(m)] for y in range(m)]

        # Each square in the first row can be reached in 1 valid way
        for i in range(len(sub_prob_mt)):
            sub_prob_mt[0][i] = 1

        # Each square in the first column can be reached in 1 valid way
        for i in range(len(sub_prob_mt[0])):
            sub_prob_mt[i][0] = 1

        for i in range(1, len(sub_prob_mt)):
            for j in range(1, len(sub_prob_mt[0])):
                # The number of ways to reach any other square on the grib is the sum of the
                # ways to reach the square above it and the ways to reach the square below it
                sub_prob_mt[i][j] = sub_prob_mt[i - 1][j] + \
                    sub_prob_mt[i][j - 1]

        return sub_prob_mt[-1][-1]
