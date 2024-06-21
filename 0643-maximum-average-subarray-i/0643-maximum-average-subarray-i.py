class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Step 1: Calculate the sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Step 2: Slide the window across the array
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
        
        # Step 3: Calculate and return the maximum average
        return max_sum / float(k)
