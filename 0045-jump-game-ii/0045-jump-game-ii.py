class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Edge case: if the array has only one element, we are already at the last index
        if n == 1:
            return 0
        
        # Initialize variables
        jumps = 0       # Number of jumps needed to reach the end
        current_end = 0 # The furthest index we can reach with the current number of jumps
        farthest = 0    # The furthest index we can reach with the next jump
        
        for i in range(n):
            # Update the furthest index we can reach with the next jump
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current range
            if i == current_end:
                # We need to make another jump
                jumps += 1
                current_end = farthest
                # If the current_end is at or beyond the last index, we are done
                if current_end >= n - 1:
                    break
        
        return jumps
