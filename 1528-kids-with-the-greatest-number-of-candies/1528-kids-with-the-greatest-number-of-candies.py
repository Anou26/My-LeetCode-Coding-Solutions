class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Step 1: Find the maximum candies count any kid currently has
        max_candies = max(candies)
        
        # Step 2: Initialize the result list
        result = []
        
        # Step 3: Iterate through each kid's candies
        for candy in candies:
            # Check if the current kid's candies + extraCandies is greater than or equal to max_candies
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        # Step 4: Return the result list
        return result
