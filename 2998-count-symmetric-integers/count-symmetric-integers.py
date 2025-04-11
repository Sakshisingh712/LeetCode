class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1, 1):
            n = len(str(num))
            if n % 2 == 0:
                firstN, lastN = 0, 0
                for i, digit in enumerate(str(num)):
                    if i < (n//2):
                        firstN += int(digit)
                    else:
                        lastN += int(digit)      
                if firstN == lastN:
                    count += 1
        return count