class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < 0:
                maxProd, minProd = minProd, maxProd
            maxProd = max(curr, curr * maxProd)
            minProd = min(curr, curr * minProd)
            res =  max(res, maxProd)
        return res