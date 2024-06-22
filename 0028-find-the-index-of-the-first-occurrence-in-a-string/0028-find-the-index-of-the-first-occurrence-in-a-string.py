class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Use the find method to get the first occurrence of needle in haystack
        return haystack.find(needle)
