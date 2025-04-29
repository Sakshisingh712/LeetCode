class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxSum = float('-inf')
        maxCurr = float('-inf')

        for i in range(len(nums)):
            maxCurr = max(maxCurr + nums[i], nums[i] )
            maxSum = max(maxSum, maxCurr)
        return maxSum
            
                


        