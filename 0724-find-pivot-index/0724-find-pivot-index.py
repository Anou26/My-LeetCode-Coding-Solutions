class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # Calculate the right sum by subtracting the left sum and the current element from the total sum
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            
            # Update the left sum for the next iteration
            left_sum += nums[i]
        
        return -1

# Example usage
solution = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(solution.pivotIndex(nums))  # Output: 3

nums = [1, 2, 3]
print(solution.pivotIndex(nums))  # Output: -1

nums = [2, 1, -1]
print(solution.pivotIndex(nums))  # Output: 0
