class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, n):
            if n == 0:
                return 1
            if n < 0:
                x = 1 / x
                n = -n
            if n % 2 == 0:
                half = power(x, n // 2)
                return half * half
            else:
                half = power(x, (n - 1) // 2)
                return half * half * x
        
        return power(x, n)
