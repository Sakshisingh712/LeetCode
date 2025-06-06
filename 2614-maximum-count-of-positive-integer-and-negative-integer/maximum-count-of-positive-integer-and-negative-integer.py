class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        res = 0
        if set(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]>0:
                pos += 1
            elif nums[i]<0:
                neg += 1
            res = max(pos, neg)
        return res
            

