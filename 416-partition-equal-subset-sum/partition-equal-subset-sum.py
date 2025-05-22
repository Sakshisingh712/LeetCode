class Solution:
    def subsetSum(self, nums, sums):
        n = len(nums)
        dp = [[False for _ in range(sums + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(sums + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and j > 0:
                    dp[i][j] = False
                elif j == 0 and i > 0:
                    dp[i][j] = True

        for i in range(1, n + 1):
            for j in range(1, sums + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][sums]

    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        else:
            return self.subsetSum(nums, sums//2)

