class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize the set to store characters in the current window
        char_set = set()
        # Initialize pointers for the sliding window
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If the character is already in the set, remove the leftmost character until it's not in the set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length

# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
