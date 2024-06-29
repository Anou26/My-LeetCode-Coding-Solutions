class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # adjusting to 1-based index
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        # No solution found if we exit the loop
        return [-1, -1]  # Optional, as the problem guarantees exactly one solution
