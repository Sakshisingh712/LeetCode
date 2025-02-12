class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summation = sum(nums)
        prefixsum = 0
        # for i in range(len(nums)):
        #     summation = summation + nums[i]
        for j in range(len(nums)):
            if summation - nums[j] == 0 and j==0 :
                return  0
            elif prefixsum == (summation - nums[j]):
                return j
            elif prefixsum == 0 and j==len(nums)-1:
                return j
            else:
                prefixsum += nums[j]
                summation -= nums[j]
        return -1