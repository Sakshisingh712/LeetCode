class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        usedBit = 0
        windowStart = 0
        maxLen = 0
        for winEnd in range(len(nums)):
            while nums[winEnd] & usedBit != 0:
                usedBit ^= nums[windowStart]
                windowStart += 1
            usedBit |= nums[winEnd]
            maxLen = max(maxLen, winEnd - windowStart + 1)
        return maxLen
