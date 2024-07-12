class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = '#'  # Mark the cell as visited
            found = (dfs(board, word, i+1, j, k+1) or
                     dfs(board, word, i-1, j, k+1) or
                     dfs(board, word, i, j+1, k+1) or
                     dfs(board, word, i, j-1, k+1))
            board[i][j] = temp  # Restore the cell
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True
        return False
