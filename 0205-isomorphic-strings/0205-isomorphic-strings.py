class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Early exit if lengths of s and t are not equal
        if len(s) != len(t):
            return False
        
        # Create two dictionaries to store mappings of characters from s to t and t to s
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Check if there is a mismatch in the mapping from s to t
            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                mapping_s_to_t[char_s] = char_t
            
            # Check if there is a mismatch in the mapping from t to s
            if char_t in mapping_t_to_s:
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                mapping_t_to_s[char_t] = char_s
        
        return True
