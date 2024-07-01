class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        
        # Compute the products of all elements to the left of each element
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Compute the products of all elements to the right of each element
        # and multiply with the corresponding left products
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer

# Example usage:
# sol = Solution()
# print(sol.productExceptSelf([1,2,3,4]))  # Output: [24, 12, 8, 6]
# print(sol.productExceptSelf([-1,1,0,-3,3]))  # Output: [0, 0, 9, 0, 0]
  