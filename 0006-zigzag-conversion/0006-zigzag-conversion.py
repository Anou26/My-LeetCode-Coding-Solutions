class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array to hold the rows
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate over the characters in the string
        for char in s:
            rows[current_row] += char
            # Change direction if we are at the first or last row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1

        # Combine all rows to get the final string
        return ''.join(rows)
