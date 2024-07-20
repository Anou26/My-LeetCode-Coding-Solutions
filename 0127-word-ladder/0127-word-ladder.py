from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # If the endWord is not in the wordList, return 0
        if endWord not in wordList:
            return 0
        
        # Convert wordList to a set for O(1) look-ups
        wordSet = set(wordList)
        
        # Queue for BFS: stores tuples of (current word, current length of transformation sequence)
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, length = queue.popleft()
            
            # Try all possible single letter transformations
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Change one character at position i
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    # If the transformed word is the endWord, return the length + 1
                    if next_word == endWord:
                        return length + 1
                    
                    # If the transformed word is in the word set, add it to the queue
                    if next_word in wordSet:
                        queue.append((next_word, length + 1))
                        wordSet.remove(next_word)
        
        # If no transformation sequence is found, return 0
        return 0
