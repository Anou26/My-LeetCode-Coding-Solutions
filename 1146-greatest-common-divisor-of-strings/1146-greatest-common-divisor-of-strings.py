class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def canDivide(s, t):
            if len(s) % len(t) != 0:
                return False
            return t * (len(s) // len(t)) == s
        
        gcd_length = gcd(len(str1), len(str2))
        candidate = str1[:gcd_length]
        
        if canDivide(str1, candidate) and canDivide(str2, candidate):
            return candidate
        return ""

# Examples to test the function
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))    # Output: ""
