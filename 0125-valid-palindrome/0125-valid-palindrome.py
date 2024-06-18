class Solution(object):
    def isPalindrome(self, s):
        
        # Convert to lowercase and filter out non-alphanumeric characters
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Check if the filtered list is equal to its reverse
        return filtered_chars == filtered_chars[::-1]
        