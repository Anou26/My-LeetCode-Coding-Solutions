class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Create a dictionary to map Roman numerals to integers
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Step 2: Initialize the total to 0
        total = 0
        length = len(s)
        
        # Step 3: Iterate through the string
        for i in range(length):
            # Step 4: Check if this is a subtractive combination
            if i < length - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                # Subtractive case
                total -= roman_to_int[s[i]]
            else:
                # Regular case
                total += roman_to_int[s[i]]
        
        return total
