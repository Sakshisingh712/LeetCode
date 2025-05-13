class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        from collections import Counter
        mod = 10 ** 9 + 7
        length = len(s)

        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1
        
        for  _ in range(t):
            temp = [0] * 26
            for i in range(26):
                if i == 25:
                    temp[0] = (temp[0] + count[i]) % mod
                    temp[1] = (temp[1] + count[i]) % mod
                else:
                    temp[i + 1] = (temp[i + 1] + count[i]) % mod
            count = temp
        return sum(count) % mod
        
        # for _ in range(t):
            
            