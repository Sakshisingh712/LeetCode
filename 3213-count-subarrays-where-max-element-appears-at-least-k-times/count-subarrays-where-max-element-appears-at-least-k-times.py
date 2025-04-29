class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEle = max(nums)
        left, right = 0, 0
        n = len(nums)
        ans = 0
        freq = 0
        # print(nums[left], nums[right])
        while right < n:
            # print(nums[left], nums[right], freq)
            if nums[right] == maxEle:
                freq += 1
        
            while freq == k:
                if nums[left] == maxEle:
                    freq -= 1
                    # print(freq, left)
                left += 1
            print(left, right)
            ans += left
            right += 1
        return ans