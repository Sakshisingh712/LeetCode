class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i, max_d, res = 0, 0, 0
        n = len(nums)
        for k in range(n):
            res = max(res, max_d*nums[k])
            max_d = max(max_d, max_i - nums[k])
            max_i = max(max_i, nums[k])
        return res