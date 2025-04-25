class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = 0
        cnt = Counter([0])
        # print(cnt)
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] % modulo == k:
                prefix += 1
            else:
                prefix += 0
            ans += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return ans