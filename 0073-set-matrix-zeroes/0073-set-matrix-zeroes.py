class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Variables to mark if first row and first column should be zeroed
        first_row_zero = False
        first_col_zero = False
        
        # Determine if first row or first column needs to be zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Use first row and column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set matrix cells to zero based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle the first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Handle the first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
