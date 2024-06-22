from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count the frequency of each character in ransomNote and magazine
        ransomNoteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        
        # Check if each character in ransomNote has enough occurrences in magazine
        for char, count in ransomNoteCounter.items():
            if magazineCounter[char] < count:
                return False
        
        return True

        