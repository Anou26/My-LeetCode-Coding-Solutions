from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        # Count the frequency of each character in t
        dict_t = Counter(t)

        # Number of unique characters in t that must be present in the window
        required = len(dict_t)

        # Initialize the left and right pointer and formed count
        left, right = 0, 0
        formed = 0

        # Dictionary to keep track of the characters in the current window
        window_counts = {}

        # (window length, left, right)
        ans = float("inf"), None, None

        while right < len(s):
            # Add one character from the right to the window
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added matches the desired count in t
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try to contract the window until it ceases to be 'desirable'
            while left <= right and formed == required:
                character = s[left]

                # Save the smallest window so far
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # The character at the position pointed by the `left` pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead to look for a new window
                left += 1    

            # Keep expanding the window by moving the right pointer
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
