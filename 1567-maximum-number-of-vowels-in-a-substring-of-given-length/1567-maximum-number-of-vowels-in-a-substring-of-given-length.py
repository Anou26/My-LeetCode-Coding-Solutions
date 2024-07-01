class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_vowel_count = 0
        max_vowel_count = 0

        # Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowel_count += 1
        
        max_vowel_count = current_vowel_count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowel_count += 1
            if s[i - k] in vowels:
                current_vowel_count -= 1
            
            max_vowel_count = max(max_vowel_count, current_vowel_count)
        
        return max_vowel_count

# Example usage:
# sol = Solution()
# print(sol.maxVowels("abciiidef", 3))  # Output: 3
# print(sol.maxVowels("aeiou", 2))  # Output: 2
# print(sol.maxVowels("leetcode", 3))  # Output: 2
