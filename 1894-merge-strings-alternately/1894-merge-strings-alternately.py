class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        len1, len2 = len(word1), len(word2)
        
        # Iterate through both strings and add letters alternately
        for i in range(max(len1, len2)):
            if i < len1:
                merged.append(word1[i])
            if i < len2:
                merged.append(word2[i])
        
        # Join the list into a single string and return
        return ''.join(merged)

# Example usage:
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
