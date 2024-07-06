class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack = []
        string_stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                count_stack.append(current_num)
                string_stack.append(current_string)
                current_string = ""
                current_num = 0
            elif char == ']':
                repeat_count = count_stack.pop()
                last_string = string_stack.pop()
                current_string = last_string + current_string * repeat_count
            else:
                current_string += char
        
        return current_string
