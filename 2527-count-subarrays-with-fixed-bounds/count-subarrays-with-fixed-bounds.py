class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min = last_max = last_invalid = -1
        count = 0
        for i, x in enumerate(nums):
            if x < minK or x > maxK: 
                last_invalid = i
            if x == minK:            
                last_min = i
            if x == maxK:            
                last_max = i
            count += max(0, min(last_min, last_max) - last_invalid)
        return count