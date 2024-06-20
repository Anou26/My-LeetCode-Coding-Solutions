class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# Example usage:
solution = Solution()

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices1))  # Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

# Example 2
prices2 = [7, 6, 4, 3, 1]
print(solution.maxProfit(prices2))  # Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
