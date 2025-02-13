class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_val = float('-inf')
        i = 0
        res = 0
        if len(nums)==1 and k==len(nums):
            return float(nums[0])
        for j in range(len(nums)):
            if j-i+1<=k:
                res = res + nums[j]
                max_val = res
                # print(res)
            else:
                # print(res)
                res = res + nums[j] 
                res = res - (nums[i])
                # print(i, j, res)
                i+=1
            # print(max_val)
                max_val = max(max_val, res)
        return max_val/k
        