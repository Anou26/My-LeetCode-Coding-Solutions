class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to hold the mappings of closing to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        # Loop through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket in the string does not match the top element in the stack
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets have been matched
        return not stack
