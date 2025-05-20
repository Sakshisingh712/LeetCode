class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diffArray = [0] * (n + 1)
        for l, r in queries:
            diffArray[l] += 1
            diffArray[r + 1] -= 1

        OpsCount = []
        curr = 0
        for ele in diffArray:
            curr += ele
            OpsCount.append(curr)
        
        for ops, target in zip(OpsCount, nums):
            if ops < target:
                return False
            
        return True