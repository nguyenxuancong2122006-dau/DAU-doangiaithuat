class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        expected = set(range(1, n + 1))
        
        # check từng hàng
        for row in matrix:
            if set(row) != expected:
                return False
        
        # check từng cột
        for col in range(n):
            column = set(matrix[row][col] for row in range(n))
            if column != expected:
                return False
        
        return True