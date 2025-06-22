class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        partitioned = []
        curr = 0
        while curr < n:
            partitioned.append(s[curr : curr + k])
            curr += k
        partitioned[-1] += fill  * (k - len(partitioned[-1]))
        return partitioned
        # p = 0
        # print(n//k)
        # for i in range(n//k):
        #     # print(i)
        #     temp = ''
        #     if len(s) < k:
        #         break
        #     for j in range(k):
        #         temp += s[j]
        #         # print(temp)
        #     s = s.replace(temp, '')
        #     partitioned.append(temp)
        # if len(s) != 0:
        #     diff = k - len(s)
        #     temp = s
        #     for i in range(diff):
        #         temp += fill
        #     partitioned.append(temp)
        # return partitioned

