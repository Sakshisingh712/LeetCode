from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        max_value = 0
        max_i = nums[0]  # Maximum value of nums[i] seen so far
        min_diff = float('-inf')  # Maximum (nums[i] - nums[j]) seen so far
        
        for j in range(1, n - 1):
            min_diff = max(min_diff, max_i - nums[j])
            max_value = max(max_value, min_diff * nums[j + 1])
            max_i = max(max_i, nums[j])
        
        return max_value