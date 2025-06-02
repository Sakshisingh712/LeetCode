class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(0, min(n, limit) + 1):
            ans += max(min(limit, n-i) - max(0, n - i - limit) + 1, 0)
        return ans