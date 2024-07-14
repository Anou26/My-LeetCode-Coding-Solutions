class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Sort the points based on the end coordinate
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for xstart, xend in points[1:]:
            if xstart > current_end:
                arrows += 1
                current_end = xend
        
        return arrows
