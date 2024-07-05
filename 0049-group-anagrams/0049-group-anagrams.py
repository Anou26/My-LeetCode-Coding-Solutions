class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        # Create a default dictionary where each value is a list
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word and use it as a key
            sorted_word = tuple(sorted(word))
            # Append the original word to the corresponding list in the dictionary
            anagrams[sorted_word].append(word)
        
        # Return the values of the dictionary which are lists of anagrams
        return list(anagrams.values())
