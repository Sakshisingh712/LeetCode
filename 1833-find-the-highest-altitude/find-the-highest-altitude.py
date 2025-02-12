class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        i = 0
        max_val, altitude = 0, 0
        while i<len(gain):
            altitude = altitude + gain[i]
            max_val = max(max_val, altitude)
            # print(max_val)
            i+=1
        return max_val 