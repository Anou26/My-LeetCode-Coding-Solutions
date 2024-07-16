class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = {}
        
        # Create a dictionary with the count of each word in words
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        results = []
        
        # Slide over the string in windows of total_length
        for i in range(len(s) - total_length + 1):
            seen = {}
            j = 0
            while j < num_words:
                word_index = i + j * word_length
                word = s[word_index:word_index + word_length]
                
                if word in word_count:
                    if word in seen:
                        seen[word] += 1
                    else:
                        seen[word] = 1
                    
                    # If the word appears more times than it is supposed to, break
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
                
                j += 1
            
            # If all words are matched
            if j == num_words:
                results.append(i)
        
        return results
