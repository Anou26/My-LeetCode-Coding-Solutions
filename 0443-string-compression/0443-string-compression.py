class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            # Count the number of occurrences of the current character
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character to the `write` position
            chars[write] = char
            write += 1
            
            # If count is greater than 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
