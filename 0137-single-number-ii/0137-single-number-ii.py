class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for num in nums:
            # Add num to twos if it exists in ones
            twos |= ones & num
            # XOR num with ones (add to ones if not already present, remove if present)
            ones ^= num
            # Remove bits that have appeared three times
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones
