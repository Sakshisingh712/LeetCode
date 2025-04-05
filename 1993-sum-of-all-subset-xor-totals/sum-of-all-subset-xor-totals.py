class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # else:
        def xorSum(index, nums, currentSum):
            if len(nums) == index:
                return currentSum
            
            withCurrent = xorSum(index + 1, nums, currentSum ^ nums[index])
            withoutCurrent = xorSum(index + 1, nums, currentSum)
            return withCurrent + withoutCurrent
        return xorSum(0, nums, 0)