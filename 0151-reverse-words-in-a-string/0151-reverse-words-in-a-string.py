class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Trim leading and trailing spaces, split by one or more spaces
        words = s.strip().split()
        # Reverse the list of words and join with a single space
        return ' '.join(reversed(words))
