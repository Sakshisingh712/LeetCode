class Solution:
    def maxDifference(self, s: str) -> int:
        memo = Counter(s)
        oddFreq, evenFreq = float('-inf'), float('inf')
        for i, val in memo.items():
            if val % 2 == 0:
                evenFreq = min(evenFreq, val)
            else:
                oddFreq = max(oddFreq, val)
        print(oddFreq, evenFreq)
        return oddFreq - evenFreq