import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ternary = []
        while n:
            rem = n % 3
            n = n//3
            
            if rem<0:
                n += 1
            ternary.append(rem)  
        
        if 2 not in ternary:
            return True
        return False