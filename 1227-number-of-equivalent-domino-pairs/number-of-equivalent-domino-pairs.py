class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        memo = [0] * 100
        res = 0
        for x, y in dominoes:
            if x <= y:
                val = x * 10 + y
            else:
                val = y * 10 + x
            res += memo[val]
            memo[val] += 1
        return res