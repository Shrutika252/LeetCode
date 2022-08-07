class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if target==matrix[i][-1]:
                return True
            elif target<matrix[i][-1]:
                for j in range(len(matrix[i])):
                    if target==matrix[i][j]:
                        return True
        return False