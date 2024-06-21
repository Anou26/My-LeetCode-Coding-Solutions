class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or if it's the edge of the flowerbed
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    # Plant a flower here
                    flowerbed[i] = 1
                    n -= 1
                    # If we have planted all required flowers, return true
                    if n == 0:
                        return True
        
        # If we finished the loop and haven't planted all flowers, return false
        return n <= 0
