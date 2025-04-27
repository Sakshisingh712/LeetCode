class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left = 0
        right = 0
        n =  len(nums)
        count = 0
        while right < n:
            if right - left == 2:
                # print(2*(nums[left] - nums[right]))
                if 2 * (nums[right] + nums[left]) == nums[right - 1]:
                    count += 1
                left += 1
            right += 1
        return count