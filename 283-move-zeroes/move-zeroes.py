class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==1:
            return nums
        else:
            # ptr1, ptr2 = 0, n-1
            # temp = 0
            for i in range(n):
                if nums[i]==0:
                    temp = nums[i]
                    nums.remove(nums[i])
                    # print(temp)
                    nums.append(temp)
            return nums
