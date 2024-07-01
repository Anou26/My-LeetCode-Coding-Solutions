from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # Check if both strings have the same unique characters
        if set(word1) != set(word2):
            return False
        
        # Count the frequency of each character in both strings
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        # Compare the sorted frequency counts
        return sorted(counter1.values()) == sorted(counter2.values())

# Example usage:
# sol = Solution()
# print(sol.closeStrings("abc", "bca"))  # Output: true
# print(sol.closeStrings("a", "aa"))  # Output: false
# print(sol.closeStrings("cabbba", "abbccc"))  # Output: true
