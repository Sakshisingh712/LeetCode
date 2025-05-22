class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        n = len(nums)
        if sums % 2 != 0:
            return False
        else:
            target = sums // 2
            dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
            for i in range(n + 1):
                for j in range(target + 1):
                    dp[i][0] = True

            for i in range(1, n + 1):
                for j in range(1, target + 1):
                    if nums[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
            return dp[n][target]


