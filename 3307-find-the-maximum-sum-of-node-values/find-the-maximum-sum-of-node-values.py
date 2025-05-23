class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][0] = - float('inf')
        dp[n][1] = 0

        for index in range(n - 1, -1, -1):
            for isEven in range(2):
                opsDone = dp[index + 1][isEven ^ 1] + (nums[index] ^ k)
                opsNotDone = dp[index + 1][isEven] + nums[index]
                dp[index][isEven] = max(opsDone, opsNotDone)

        return dp[0][1]