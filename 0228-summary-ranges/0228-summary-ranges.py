class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ranges = []
        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append("{}->{}".format(start, end))
                start = nums[i]
                end = nums[i]
        
        # Add the last range
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append("{}->{}".format(start, end))

        return ranges
