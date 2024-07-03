class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # The furthest point we can currently reach
        max_reach = 0
        
        for i in range(len(nums)):
            # If the current index is greater than the furthest point we can reach, return False
            if i > max_reach:
                return False
            # Update the furthest point we can reach from the current position
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach or go beyond the last index, return True
            if max_reach >= len(nums) - 1:
                return True
        
        # If we finish the loop without finding a way to reach the end, return False
        return False
