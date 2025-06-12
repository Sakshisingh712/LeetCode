class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        output = float('-inf')
        for i in range(1, len(nums)):    
            output = max(output, abs(nums[i] - nums[i-1]))
        output = max(output, abs(nums[len(nums) - 1] - nums[0]))
        return output