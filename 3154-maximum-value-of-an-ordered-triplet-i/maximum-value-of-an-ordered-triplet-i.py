from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
            n = len(nums)
            max_value = 0
            
            # Maintain the maximum prefix value nums[i] up to index j
            max_prefix = [0] * n
            max_prefix[0] = nums[0]
            for i in range(1, n):
                max_prefix[i] = max(max_prefix[i - 1], nums[i])
            
            # Traverse to find the maximum triplet value
            for j in range(1, n - 1):
                for k in range(j + 1, n):
                    max_value = max(max_value, (max_prefix[j - 1] - nums[j]) * nums[k])
            
            return max_value