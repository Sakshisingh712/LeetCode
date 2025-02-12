class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        i= 0
        j= len(nums)-1
        count = 0
        if len(nums)<1:
            return 0
        while i<j:
            value = nums[i] + nums[j] 
            if nums[j]>k or value > k:
                j-=1
            elif value == k:
                count+=1
                i+=1
                j-=1
            else:
                i+=1
            # if nums[i] + nums[j] == k:
            #     count+=1
            #     i+=1
            #     j-=1
            # elif nums[i] + nums[j] > k:
            #     j-=1
            # else:
            #     i+=1
        return count
        