import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #prime = ['2','3','5','7']
        #even = ['0','2', '4', '6', '8']
        mod = 10**9 + 7
        evenPos = math.ceil(n/2)
        oddPos = math.floor(n/2)
        # print(evenPos, oddPos)
        res = (pow(5, evenPos, mod)) * (pow(4, oddPos, mod))  % mod
        return res
        
            
