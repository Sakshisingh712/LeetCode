class Solution:
    def reverse(self, x: int) -> int:
        new = 0
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        while x > 0:
            new = new * 10 + (x % 10)
            x = x // 10
        if new > (pow(2, 31) - 1) or new < (-pow(2, 31)):
            return 0
        return -new if neg else new