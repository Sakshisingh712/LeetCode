class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        left = 0
        right = 1
        pairs = 0
        n = len(nums)
        while left < n:
            while right < n:
                # print(left, right)
                if (left * right) % k == 0 and nums[left] == nums[right]:
                    pairs += 1
                right += 1
            left += 1
            right = left + 1
        return pairs

            
            
