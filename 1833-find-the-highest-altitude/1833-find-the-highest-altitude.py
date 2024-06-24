class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        highest_altitude = 0
        
        for net_gain in gain:
            current_altitude += net_gain
            highest_altitude = max(highest_altitude, current_altitude)
        
        return highest_altitude

# Example usage
solution = Solution()
gain = [-5, 1, 5, 0, -7]
print(solution.largestAltitude(gain))  # Output: 1

gain = [-4, -3, -2, -1, 4, 3, 2]
print(solution.largestAltitude(gain))  # Output: 0
