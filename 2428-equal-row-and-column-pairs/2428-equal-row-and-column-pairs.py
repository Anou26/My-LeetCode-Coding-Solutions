class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        n = len(grid)
        row_map = defaultdict(int)
        col_map = defaultdict(int)

        # Store each row in the row_map
        for row in grid:
            row_tuple = tuple(row)
            row_map[row_tuple] += 1
        
        # Store each column in the col_map
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            col_tuple = tuple(col)
            col_map[col_tuple] += 1
        
        # Count the number of equal pairs
        count = 0
        for row_tuple in row_map:
            if row_tuple in col_map:
                count += row_map[row_tuple] * col_map[row_tuple]
        
        return count
