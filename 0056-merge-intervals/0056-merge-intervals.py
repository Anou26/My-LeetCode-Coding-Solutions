class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the list to hold the merged intervals
        merged_intervals = []
        
        for interval in intervals:
            # If merged_intervals is empty or the current interval does not overlap with the previous, append it
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                # If there is an overlap, merge the current interval with the previous one
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        return merged_intervals
