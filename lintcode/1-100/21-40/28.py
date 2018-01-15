class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return False
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[i]) - 1]:
                break
        for j in range(len(matrix[i])):
            if target == matrix[i][j]:
                break
        if target != matrix[i][j]:
            return False

        return True


obj = Solution()
print(obj.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7))
