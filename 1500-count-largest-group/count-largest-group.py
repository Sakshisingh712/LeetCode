class Solution:
    def countLargestGroup(self, n: int) -> int:
        arr = collections.Counter()
        for i in range(1, n + 1):
            val = sum([int(x) for x in str(i)])
            arr[val] += 1
        maxValue = max(arr.values())
        count = sum(1 for v in arr.values() if v == maxValue)
        return count