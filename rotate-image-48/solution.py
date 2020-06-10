from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Flip the matrix
        self.flipMatrix(matrix)

        # Transpose the matrix (i.e. cause the rows and columns to change places with each other)
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def flipMatrix(self, matrix):
        # [:] slices the entire list in place
        # [::-1] reverses the list
        matrix[:] = matrix[::-1]
