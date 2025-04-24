class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        pvt = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                pvt = i
                break
        if pvt == -1:
            nums[:] = nums[:][::-1]
            return
        for j in range(n - 1, pvt, -1):
            if nums[j] > nums[pvt]:
                nums[j], nums[pvt] = nums[pvt], nums[j]
                break
        nums[pvt + 1:] = nums[pvt + 1: ][::-1]