class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        left = right = 0
        count = ans = 0 
        mapping = defaultdict(int)
        n = len(nums)
        while right<n:
            count += mapping[nums[right]]
            mapping[nums[right]] += 1
            while left <  n and (count - (mapping[nums[left]] - 1)) >= k:
                mapping[nums[left]] -= 1
                count -= mapping[nums[left]]
                left += 1
            if count >= k:
                ans += (left + 1)
            right += 1
        return ans