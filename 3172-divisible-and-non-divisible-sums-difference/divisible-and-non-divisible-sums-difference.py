class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        x = n // m
        divTotal = int((x/2) * ((2 * m) + ((x - 1) * m)))
        total = int(n/2 * ((2*1) + (n - 1)))
        # print(total)
        nonDiv = total - divTotal
        return nonDiv - divTotal

