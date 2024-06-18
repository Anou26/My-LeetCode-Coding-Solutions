class Solution(object):
    def majorityElement(self, nums):
        # Step 1: Find a candidate for the majority element
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # Since the problem guarantees that a majority element exists, we don't need to verify the candidate
        
        return candidate
                

            
        