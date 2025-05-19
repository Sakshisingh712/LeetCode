class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            # if nums[0] == nums[1] and nums[1] == nums[2]:
            if len(set(nums)) == 1:
                return 'equilateral'
            elif len(set(nums)) == 2:
            # nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
                return 'isosceles'
            elif len(set(nums)) == 3:
            # nums[0] != nums[1] and nums[1] != nums[2] and nums[2] != nums[0]:
                return 'scalene'
        else:
            return 'none'