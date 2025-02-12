class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        i, j = 0, len(nums)-1
        count = 0
        if len(nums)<1:
            return 0
        while i<j:
            if nums[j]>k or nums[i] + nums[j]  > k:
                j-=1
            elif nums[i] + nums[j]  == k:
                count+=1
                i+=1
                j-=1
            else:
                i+=1
        return count
        