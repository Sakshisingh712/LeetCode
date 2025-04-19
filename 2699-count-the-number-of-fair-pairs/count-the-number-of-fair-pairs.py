class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # nums = list(set(nums))
        # sorted(nums)
        nums.sort()
        left = 0
        right = len(nums) - 1
        countLeft = 0
        countRight = 0
        while left < right:
            if nums[left] + nums[right] <= upper:
                countRight += (right - left)
                left += 1
            else:
                right -= 1

        left = 0
        right = len(nums) - 1
        while  left < right:
            if nums[left] + nums[right] < lower:
                countLeft += (right - left)
                left += 1
            else:
                right -= 1
        return countRight - countLeft 

            
        # while left < len(nums):
        #     right = left + 1
        #     while right < len(nums):
        #         sums = nums[left] + nums[right]
        #         if sums >= lower and sums <= upper:
        #             count += 1
        #         right += 1
        #     left += 1
        # return count
        # left = 0
        # count = 0
        # right = len(nums) - 1
        # while left < right:
        #     sums = nums[left] + nums[right]
        #     if lower <= sums <= upper:
        #             count += 1
        #             left += 1
        #     elif sums < lower:
        #         left += 1
        #     else:
        #         right -= 1
        # print(count)