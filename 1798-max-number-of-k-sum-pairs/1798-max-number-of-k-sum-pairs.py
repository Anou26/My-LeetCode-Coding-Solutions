class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        
        # Create a frequency counter for the numbers
        num_counts = Counter(nums)
        operations = 0
        
        for num in list(num_counts.keys()):
            complement = k - num
            if complement in num_counts:
                if num == complement:
                    # If num and complement are the same, form pairs from half of the total count
                    operations += num_counts[num] // 2
                else:
                    # Count pairs from the minimum of the two counts
                    pairs = min(num_counts[num], num_counts[complement])
                    operations += pairs
                    # Remove the pairs from the counter to avoid double counting
                    num_counts[num] -= pairs
                    num_counts[complement] -= pairs
        
        return operations

# Example usage:
sol = Solution()
print(sol.maxOperations([1,2,3,4], 5))  # Output: 2
print(sol.maxOperations([3,1,3,4,3], 6))  # Output: 1
