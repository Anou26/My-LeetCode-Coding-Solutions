class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # Split the string s into words
        words = s.split()
        
        # Early exit if the number of pattern characters and words do not match
        if len(pattern) != len(words):
            return False
        
        # Create two dictionaries to store mappings
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            # Check if there is a mismatch in the mapping from char to word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # Check if there is a mismatch in the mapping from word to char
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True
