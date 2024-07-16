class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        current_number = 0
        result = 0
        sign = 1  # 1 means positive, -1 means negative
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                # Push the result and the sign
                stack.append(result)
                stack.append(sign)
                # Reset the result and sign for the new sub-expression
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_number
                current_number = 0
                # Pop the sign and compute the result
                result *= stack.pop()  # stack.pop() is the sign before the parenthesis
                result += stack.pop()  # stack.pop() now is the result calculated before the parenthesis
        
        # Add the last accumulated number
        result += sign * current_number
        return result
