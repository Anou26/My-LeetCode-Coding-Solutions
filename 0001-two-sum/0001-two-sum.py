class Solution(object):
    def twoSum(self, nums, target):
        # Dictionary to store the complement and its index
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_to_index:
                # If found, return the indices
                return [num_to_index[complement], index]
            
            # Otherwise, add the number and its index to the dictionary
            num_to_index[num] = index

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
