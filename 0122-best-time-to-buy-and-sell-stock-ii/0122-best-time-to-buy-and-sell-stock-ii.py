class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

# Example usage
prices1 = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices1))  # Output: 7

prices2 = [1, 2, 3, 4, 5]
print(Solution().maxProfit(prices2))  # Output: 4

prices3 = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices3))  # Output: 0
