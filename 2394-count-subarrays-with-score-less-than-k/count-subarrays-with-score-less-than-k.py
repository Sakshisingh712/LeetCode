class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count, left, prefix = 0, 0, 0
        right = 0
        n = len(nums)
        ans = 0
        while right < n:
            prefix += nums[right]
            count = (right - left + 1)
            while left <= right and prefix * (right - left + 1) >= k:
                prefix -= nums[left]
                left += 1
                # count -= 1
                # ans += 1
            ans += (right - left + 1)
            right += 1
            
        return ans
