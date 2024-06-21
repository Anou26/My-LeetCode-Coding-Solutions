class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Sort the list of strings
        strs.sort()
        
        # The first and last strings will have the minimum common prefix
        first = strs[0]
        last = strs[-1]
        
        i = 0
        # Compare characters of the first and last strings
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        # The common prefix is the substring from the start to the last matched character
        return first[:i]
