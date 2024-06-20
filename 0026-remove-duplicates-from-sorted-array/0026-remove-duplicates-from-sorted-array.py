class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i = 0  # Initialize the first pointer
        
        for j in range(1, len(nums)):  # Start the second pointer from the second element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1  # Since 'i' is index-based, we return 'i + 1' for the count

# Example usage:
solution = Solution()

nums1 = [1, 1, 2]
print(solution.removeDuplicates(nums1))  # Output: 2
print(nums1)  # Output: [1, 2, ...]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums2))  # Output: 5
print(nums2)  # Output: [0, 1, 2,
