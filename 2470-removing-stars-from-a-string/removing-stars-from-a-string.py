class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            res.append(s[i])
            if s[i] == '*':
                res.pop()
                res.pop()
        # print(res)
        return ''.join(res)