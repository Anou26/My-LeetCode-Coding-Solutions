class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row):
            # If we have placed queens on all rows, it's a valid solution
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    count += backtrack(row + 1)
                    remove_queen(row, col)
            return count
        
        def is_not_under_attack(row, col):
            # Check if column, main diagonal, and secondary diagonal are under attack
            return not (cols[col] or diag1[row + col] or diag2[row - col])
        
        def place_queen(row, col):
            cols[col] = 1
            diag1[row + col] = 1
            diag2[row - col] = 1
        
        def remove_queen(row, col):
            cols[col] = 0
            diag1[row + col] = 0
            diag2[row - col] = 0

        # Initialize the columns, and diagonals as not under attack
        cols = [0] * n
        diag1 = [0] * (2 * n)
        diag2 = [0] * (2 * n)
        
        # Start backtracking from the first row
        return backtrack(0)
