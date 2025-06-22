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
        