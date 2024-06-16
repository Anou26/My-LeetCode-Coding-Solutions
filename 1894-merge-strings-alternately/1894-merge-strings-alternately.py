class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        len1, len2 = len(word1), len(word2)
        i = 0
        
        # Iterate through both strings and add letters alternately
        while i < len1 and i < len2:
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1
        
        # Add remaining characters from word1 if any
        if i < len1:
            merged.extend(word1[i:])
        
        # Add remaining characters from word2 if any
        if i < len2:
            merged.extend(word2[i:])
        
        return ''.join(merged)

# Examples to test the function
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
